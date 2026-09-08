<?php
// Comprehensive ÖSYM KPSS + Generic PDF Parser Test

function parse_pdf_test($filePath) {
    $cmd = "pdftotext -layout " . escapeshellarg($filePath) . " -";
    $text = shell_exec($cmd);

    $cleanLetters = preg_replace('/[^a-zA-Z0-9\x{00C0}-\x{017F}]+/u', '', $text ?? '');
    if (mb_strlen($cleanLetters) < 50) {
        return ['error' => true, 'is_scanned' => true, 'message' => 'Taranmış görsel.'];
    }

    $pages = array_values(array_filter(explode("\x0c", $text), function($p) {
        return !empty(trim($p));
    }));
    $totalPages = count($pages);

    // Check for ÖSYM KPSS
    $isOsymKpss = (
        (stripos($text, 'GENEL YETENEK') !== false || stripos($text, 'GY-PS') !== false) &&
        (stripos($text, 'GENEL KÜLTÜR') !== false || stripos($text, 'GK-PS') !== false)
    );

    // Extract year if available
    $year = '';
    if (preg_match('/(20\d{2})[-\s]*(?:KPSS|Kamu)/iu', $text, $ym)) {
        $year = $ym[1];
    }

    if ($isOsymKpss) {
        // --- 1. FIND ANSWER KEY PAGE (usually the last page) ---
        $ansKeys = ['GY' => [], 'GK' => []];
        $ansPageIdx = -1;

        for ($p = $totalPages - 1; $p >= max(0, $totalPages - 3); $p--) {
            $pContent = $pages[$p];
            if (stripos($pContent, 'GENEL YETENEK') !== false && stripos($pContent, 'GENEL KÜLTÜR') !== false) {
                // Parse GY (left half) and GK (right half)
                $lines = explode("\n", $pContent);
                $foundAny = false;
                foreach ($lines as $l) {
                    if (preg_match_all('/(\d{1,2})\.\s+([A-E])\b/u', $l, $matches, PREG_OFFSET_CAPTURE)) {
                        foreach ($matches[1] as $idx => $m) {
                            $qnum = intval($m[0]);
                            $ansLetter = strtolower($matches[2][$idx][0]);
                            $offset = $m[1];
                            if ($offset < 50) {
                                $ansKeys['GY'][$qnum] = $ansLetter;
                            } else {
                                $ansKeys['GK'][$qnum] = $ansLetter;
                            }
                            $foundAny = true;
                        }
                    }
                }
                if ($foundAny && count($ansKeys['GY']) > 20) {
                    $ansPageIdx = $p;
                    break;
                }
            }
        }

        // --- 2. EXTRACT QUESTIONS ---
        $gy_questions = [];
        $gk_questions = [];

        for ($pno = 0; $pno < $totalPages; $pno++) {
            // Skip the answer sheet page
            if ($pno === $ansPageIdx) continue;

            $pText = $pages[$pno];
            if (empty(trim($pText))) continue;

            // Determine section: GY vs GK
            $header = substr($pText, 0, 150);
            if (strpos($header, '/GK') !== false || strpos($header, 'GK-PS') !== false) {
                $currentTest = 'GK';
            } elseif (strpos($header, '/GY') !== false || strpos($header, 'GY-PS') !== false) {
                $currentTest = 'GY';
            } elseif ($pno >= 20) {
                $currentTest = 'GK';
            } else {
                $currentTest = 'GY';
            }

            $pLines = explode("\n", $pText);
            $leftCol = [];
            $rightCol = [];

            foreach ($pLines as $line) {
                // Wide gap check
                $wideGap = false;
                if (preg_match('/\s{15,}/', substr($line, 15, 60), $wgm, PREG_OFFSET_CAPTURE)) {
                    $splitPos = 15 + $wgm[0][1] + intval(strlen($wgm[0][0]) / 2);
                    $leftCol[] = rtrim(substr($line, 0, $splitPos));
                    $rightCol[] = rtrim(substr($line, $splitPos));
                    continue;
                }

                $hasLeft = (trim(substr($line, 0, 65)) !== '');
                $hasRight = (strlen($line) > 65 && trim(substr($line, 65)) !== '');

                if ($hasLeft && $hasRight) {
                    $sub = substr($line, 50, 35);
                    if (preg_match('/\s{3,}/', $sub, $gm, PREG_OFFSET_CAPTURE)) {
                        $splitPos = 50 + $gm[0][1] + intval(strlen($gm[0][0]) / 2);
                    } else {
                        $splitPos = 68;
                    }
                    $leftCol[] = rtrim(substr($line, 0, $splitPos));
                    $rightCol[] = rtrim(substr($line, $splitPos));
                } elseif ($hasLeft) {
                    $leftCol[] = rtrim(substr($line, 0, 65));
                    $rightCol[] = '';
                } elseif ($hasRight) {
                    $leftCol[] = '';
                    $rightCol[] = rtrim(substr($line, 65));
                } else {
                    $leftCol[] = '';
                    $rightCol[] = '';
                }
            }

            $stream = array_merge($leftCol, $rightCol);
            $curQ = null;

            foreach ($stream as $l) {
                $trim = trim($l);
                if (empty($trim)) continue;

                // Skip headers/footers
                $skip = false;
                foreach (['KPSS', 'GENEL YETENEK TESTİ', 'GENEL KÜLTÜR TESTİ', 'Diğer sayfaya', 'TEST BİTTİ', 'Bu testte', 'Cevaplarınızı', 'ÖSYM'] as $kw) {
                    if (strpos($trim, $kw) !== false && strlen($trim) < 70) {
                        $skip = true;
                        break;
                    }
                }
                if ($skip) continue;

                // Match question number
                if (preg_match('/^(\d{1,2})\.(?:\s+(.*))?$/u', $trim, $qm)) {
                    $qnum = intval($qm[1]);
                    if ($qnum >= 1 && $qnum <= 60) {
                        if ($curQ) {
                            if ($curQ['test'] === 'GY') {
                                $gy_questions[$curQ['qnum']] = $curQ;
                            } else {
                                $gk_questions[$curQ['qnum']] = $curQ;
                            }
                        }

                        $ans = $ansKeys[$currentTest][$qnum] ?? 'a';
                        $qtext = $qm[2] ?? '';

                        // Subject & Category Mapping for KPSS:
                        // GY: 1-30 Türkçe (cat 4, sub 18), 31-60 Matematik (cat 5, sub 0)
                        // GK: 1-27 Tarih (cat 1, sub 1), 28-45 Coğrafya (cat 2, sub 8), 46-54 Vatandaşlık (cat 3, sub 13), 55-60 Güncel (cat 3, sub 17)
                        $cat = 0;
                        $sub = 0;
                        $subjectName = '';
                        if ($currentTest === 'GY') {
                            if ($qnum <= 30) {
                                $cat = 4;
                                $sub = 18;
                                $subjectName = 'Türkçe';
                            } else {
                                $cat = 5;
                                $sub = 0;
                                $subjectName = 'Matematik';
                            }
                        } else {
                            if ($qnum <= 27) {
                                $cat = 1;
                                $sub = 1;
                                $subjectName = 'Tarih';
                            } elseif ($qnum <= 45) {
                                $cat = 2;
                                $sub = 8;
                                $subjectName = 'Coğrafya';
                            } elseif ($qnum <= 54) {
                                $cat = 3;
                                $sub = 13;
                                $subjectName = 'Vatandaşlık';
                            } else {
                                $cat = 3;
                                $sub = 17;
                                $subjectName = 'Güncel Bilgiler';
                            }
                        }

                        $secName = ($currentTest === 'GY') ? 'Genel Yetenek' : 'Genel Kültür';
                        $yearStr = !empty($year) ? "$year " : "";
                        $solutionText = "ÖSYM {$yearStr}KPSS {$secName} ({$subjectName}) {$qnum}. Soru. Resmi Doğru Cevap: " . strtoupper($ans);

                        $curQ = [
                            'qnum' => $qnum,
                            'test' => $currentTest,
                            'category' => $cat,
                            'subcategory' => $sub,
                            'subject' => $subjectName,
                            'question' => $qtext,
                            'optiona' => '',
                            'optionb' => '',
                            'optionc' => '',
                            'optiond' => '',
                            'optione' => '',
                            'answer' => $ans,
                            'solution' => $solutionText
                        ];
                        continue;
                    }
                }

                if (!$curQ) continue;

                // Match options: A) ... B) ... etc.
                if (preg_match_all('/([A-E])\)\s*/u', $trim, $optMatches, PREG_OFFSET_CAPTURE)) {
                    $count = count($optMatches[0]);
                    for ($i = 0; $i < $count; $i++) {
                        $letter = strtolower($optMatches[1][$i][0]);
                        $start = $optMatches[0][$i][1] + strlen($optMatches[0][$i][0]);
                        $end = ($i + 1 < $count) ? $optMatches[0][$i + 1][1] : strlen($trim);
                        $optVal = trim(substr($trim, $start, $end - $start));
                        $curQ['option' . $letter] = $optVal;
                    }
                    continue;
                }

                // Append line text to current question or option
                if (empty($curQ['optiona'])) {
                    $curQ['question'] = trim($curQ['question'] . ' ' . $trim);
                } elseif (!empty($curQ['optione'])) {
                    $curQ['optione'] .= ' ' . $trim;
                } elseif (!empty($curQ['optiond'])) {
                    $curQ['optiond'] .= ' ' . $trim;
                } elseif (!empty($curQ['optionc'])) {
                    $curQ['optionc'] .= ' ' . $trim;
                } elseif (!empty($curQ['optionb'])) {
                    $curQ['optionb'] .= ' ' . $trim;
                } elseif (!empty($curQ['optiona'])) {
                    $curQ['optiona'] .= ' ' . $trim;
                }
            }

            if ($curQ) {
                if ($curQ['test'] === 'GY') {
                    $gy_questions[$curQ['qnum']] = $curQ;
                } else {
                    $gk_questions[$curQ['qnum']] = $curQ;
                }
            }
        }

        // Merge in order: GY 1-60, then GK 1-60
        ksort($gy_questions);
        ksort($gk_questions);
        $allQuestions = [];
        foreach ($gy_questions as $q) {
            // Fill empty options for math/geometry
            foreach (['a', 'b', 'c', 'd', 'e'] as $optL) {
                if (empty(trim($q['option' . $optL]))) {
                    $q['option' . $optL] = '[Matematiksel Şık ' . strtoupper($optL) . ']';
                }
            }
            $allQuestions[] = $q;
        }
        foreach ($gk_questions as $q) {
            foreach (['a', 'b', 'c', 'd', 'e'] as $optL) {
                if (empty(trim($q['option' . $optL]))) {
                    $q['option' . $optL] = '[Şık ' . strtoupper($optL) . ']';
                }
            }
            $allQuestions[] = $q;
        }

        return [
            'error' => false,
            'title' => basename($filePath),
            'year' => $year,
            'is_osym' => true,
            'gy_count' => count($gy_questions),
            'gk_count' => count($gk_questions),
            'total' => count($allQuestions),
            'questions' => $allQuestions
        ];
    }

    return ['error' => true, 'message' => 'Genel PDF'];
}

$res = parse_pdf_test('/tmp/2019.pdf');
echo "RESULT:\n";
echo "Error: " . ($res['error'] ? 'yes' : 'no') . "\n";
echo "Year: " . $res['year'] . "\n";
echo "GY count: " . $res['gy_count'] . "\n";
echo "GK count: " . $res['gk_count'] . "\n";
echo "Total questions: " . $res['total'] . "\n";

echo "\nFirst 2 GY:\n";
echo "Q1: " . $res['questions'][0]['question'] . "\n";
echo "Ans: " . $res['questions'][0]['answer'] . " | Sol: " . $res['questions'][0]['solution'] . "\n";
echo "Q2: " . $res['questions'][1]['question'] . "\n";
echo "Ans: " . $res['questions'][1]['answer'] . " | Sol: " . $res['questions'][1]['solution'] . "\n";

echo "\nFirst 2 GK:\n";
echo "Q61 (GK 1): " . $res['questions'][60]['question'] . "\n";
echo "Ans: " . $res['questions'][60]['answer'] . " | Sol: " . $res['questions'][60]['solution'] . "\n";
echo "Q62 (GK 2): " . $res['questions'][61]['question'] . "\n";
echo "Ans: " . $res['questions'][61]['answer'] . " | Sol: " . $res['questions'][61]['solution'] . "\n";
