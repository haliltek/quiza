<?php
$rawEmbed = file_get_contents('d:/quiza/scratch_osym/scribd_822947672.html');
preg_match_all('/pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"/s', $rawEmbed, $pm);
$pageUrls = [];
foreach ($pm[1] as $idx => $p) {
    $pageUrls[intval($p)] = $pm[2][$idx];
}
echo "Total Scribd Pages available for Anayasa: " . count($pageUrls) . "\n";

function parse_scribd_page($pageUrl, $pnum) {
    $ch = curl_init($pageUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 8);
    $res = curl_exec($ch);
    curl_close($ch);
    if (empty($res)) return [];
    if (substr($res, 0, 2) === "\x1f\x8b") $res = gzdecode($res);

    $res = preg_replace('/^window\.page\d+_callback\s*\(\s*\[\s*"/s', '', $res);
    $res = preg_replace('/"\s*\]\s*\)\s*;\s*$/s', '', $res);

    preg_match_all('/<span class=a style=\\\\"left:(\d+)px;top:(\d+)px;([^"]*)\\\\"[^>]*>(.*?)(?=(?:<span class=a style=\\\\"left:|<div class=ff|$))/s', $res, $matches, PREG_SET_ORDER);
    if (empty($matches)) return [];

    $items = [];
    foreach ($matches as $m) {
        $left = intval($m[1]);
        $top = intval($m[2]);
        $txt = strip_tags($m[4]);
        $txt = html_entity_decode($txt, ENT_QUOTES | ENT_HTML5, 'UTF-8');
        $txt = preg_replace('/[\r\n\t]+/', ' ', $txt);
        $txt = preg_replace('/[\x{00a0}\x{200b}\s]+/u', ' ', $txt);
        $txt = trim($txt);
        if (!empty($txt)) {
            $items[] = ['left' => $left, 'top' => $top, 'text' => $txt];
        }
    }

    usort($items, function ($a, $b) {
        if ($a['top'] == $b['top']) return $a['left'] <=> $b['left'];
        return $a['top'] <=> $b['top'];
    });

    $questions = [];
    $currentQ = null;

    foreach ($items as $item) {
        $txt = $item['text'];

        if (preg_match('/(Hakimlik|Hukuk Meslekleri|Akademisi|1\.Bölüm|Anayasa Hukuku|\b\d+\s*$)/iu', $txt) && mb_strlen($txt) < 40) {
            continue;
        }

        if (preg_match('/^(\d{1,3})\.\s*(.*)/u', $txt, $qm)) {
            if ($currentQ && !empty($currentQ['optiona']) && !empty($currentQ['answer'])) {
                $questions[] = $currentQ;
            }
            $currentQ = [
                'qnum' => intval($qm[1]),
                'page' => $pnum,
                'question' => $qm[2],
                'optiona' => '',
                'optionb' => '',
                'optionc' => '',
                'optiond' => '',
                'optione' => '',
                'solution' => '',
                'answer' => ''
            ];
            continue;
        }

        if (!$currentQ) continue;

        if (preg_match('/^[A-E]\)\s*(.*)/u', $txt)) {
            if (preg_match('/^A\)\s*(.*)/u', $txt, $om)) {
                $currentQ['optiona'] = $om[1];
                continue;
            }
            if (preg_match('/^B\)\s*(.*)/u', $txt, $om)) {
                $currentQ['optionb'] = $om[1];
                continue;
            }
            if (preg_match('/^C\)\s*(.*)/u', $txt, $om)) {
                $currentQ['optionc'] = $om[1];
                continue;
            }
            if (preg_match('/^D\)\s*(.*)/u', $txt, $om)) {
                $currentQ['optiond'] = $om[1];
                continue;
            }
            if (preg_match('/^E\)\s*(.*)/u', $txt, $om)) {
                $currentQ['optione'] = $om[1];
                continue;
            }
        }

        if (preg_match('/CEVAP\s*:\s*([A-E])/iu', $txt, $am)) {
            $currentQ['answer'] = strtolower($am[1]);
            continue;
        }

        if (preg_match('/^(ÇÖZÜM|DİKKAT)/iu', $txt)) {
            $cleanSol = preg_replace('/^(ÇÖZÜM|DİKKAT)\s*[:\-]?\s*/iu', '', $txt);
            if (!empty($cleanSol)) {
                $currentQ['solution'] .= (empty($currentQ['solution']) ? '' : ' ') . $cleanSol;
            }
            continue;
        }

        $txt = preg_replace('/[\]\)\;\"\s]+$/', '', $txt);
        $txt = trim($txt);
        if (empty($txt)) continue;

        if (!empty($currentQ['optione']) && empty($currentQ['answer'])) {
            $currentQ['solution'] .= (empty($currentQ['solution']) ? '' : ' ') . $txt;
        } else if (empty($currentQ['optiona'])) {
            $currentQ['question'] .= ' ' . $txt;
        } else if (!empty($currentQ['optiond']) && empty($currentQ['optione'])) {
            $currentQ['optiond'] .= ' ' . $txt;
        } else if (!empty($currentQ['optionc']) && empty($currentQ['optiond'])) {
            $currentQ['optionc'] .= ' ' . $txt;
        } else if (!empty($currentQ['optionb']) && empty($currentQ['optionc'])) {
            $currentQ['optionb'] .= ' ' . $txt;
        } else if (!empty($currentQ['optiona']) && empty($currentQ['optionb'])) {
            $currentQ['optiona'] .= ' ' . $txt;
        }
    }

    if ($currentQ && !empty($currentQ['optiona']) && !empty($currentQ['answer'])) {
        $questions[] = $currentQ;
    }

    return $questions;
}

$allExtracted = [];
$startTime = time();

ksort($pageUrls);
foreach ($pageUrls as $pnum => $pageUrl) {
    if ($pnum < 5) continue;
    $res = parse_scribd_page($pageUrl, $pnum);
    foreach ($res as $q) {
        $allExtracted[] = $q;
    }
    if ($pnum % 30 == 0) {
        echo "Processed through page $pnum: " . count($allExtracted) . " questions found...\n";
    }
}

echo "FINISHED! Total extracted for Anayasa: " . count($allExtracted) . " questions in " . (time() - $startTime) . "s\n";

file_put_contents('d:/quiza/scratch_osym/extracted_anayasa_book.json', json_encode($allExtracted, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
echo "Saved to d:/quiza/scratch_osym/extracted_anayasa_book.json\n";
