<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Book_Importer extends CI_Controller
{
    public function __construct()
    {
        parent::__construct();
        if (!$this->session->userdata('isLoggedIn')) {
            redirect('/');
        }
        $this->load->config('quiz');
        date_default_timezone_set(get_system_timezone());
    }

    public function index()
    {
        if (!has_permissions('read', 'questions')) {
            redirect('/');
        }

        // Fetch categories and subcategories
        $this->db->order_by('id', 'ASC');
        $data['categories'] = $this->db->get('tbl_category')->result();

        // Fetch exams from exam module if table exists
        $data['exams'] = [];
        if ($this->db->table_exists('tbl_exam_module')) {
            $this->db->order_by('id', 'DESC');
            $data['exams'] = $this->db->get('tbl_exam_module')->result();
        }

        $this->load->view('book_import', $data);
    }

    private function json_response($data)
    {
        $data['csrf_token'] = $this->security->get_csrf_token_name();
        $data['csrf_hash'] = $this->security->get_csrf_hash();
        
        $cleanData = $this->utf8ize($data);

        header('Content-Type: application/json; charset=utf-8');
        echo json_encode($cleanData, JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE);
        return;
    }

    private function utf8ize($mixed)
    {
        if (is_array($mixed)) {
            foreach ($mixed as $key => $value) {
                $mixed[$key] = $this->utf8ize($value);
            }
        } elseif (is_string($mixed)) {
            return mb_convert_encoding($mixed, 'UTF-8', 'UTF-8');
        }
        return $mixed;
    }

    public function preview()
    {
        if (!has_permissions('create', 'questions')) {
            return $this->json_response(['error' => true, 'message' => 'Yetkiniz bulunmamaktadır.']);
        }

        $url = trim($this->input->post('url') ?? '');
        $badge = trim($this->input->post('badge') ?? '');
        $category_id = intval($this->input->post('category_id') ?? 0);
        $subcategory_id = intval($this->input->post('subcategory_id') ?? 0);
        $exam_id = intval($this->input->post('exam_id') ?? 0);
        $html_source = trim($this->input->post('html_source') ?? '');

        // Handle raw HTML source paste
        if (!empty($html_source)) {
            $result = $this->parse_scribd_html_string($html_source, $badge);
            if ($result['error']) {
                return $this->json_response($result);
            }
            $this->session->set_userdata('book_import_cache', [
                'questions' => $result['questions'],
                'category_id' => $category_id,
                'subcategory_id' => $subcategory_id,
                'exam_id' => $exam_id,
                'badge' => $badge,
                'title' => $result['title']
            ]);

            return $this->json_response([
                'error' => false,
                'title' => $result['title'],
                'total' => count($result['questions']),
                'preview' => array_slice($result['questions'], 0, 30),
                'message' => count($result['questions']) . ' soru ve çözüm kaynak kodundan başarıyla analiz edildi.'
            ]);
        }

        if (empty($url) && empty($_FILES['pdf_file']['name'])) {
            return $this->json_response(['error' => true, 'message' => 'Lütfen geçerli bir kitap linki (Scribd/PDF) girin veya PDF yükleyin.']);
        }

        // Handle Scribd URL
        if (!empty($url) && strpos($url, 'scribd.com') !== false) {
            $result = $this->parse_scribd_url($url, $badge);
            if ($result['error']) {
                return $this->json_response($result);
            }
            // Store preview in session for 1-click import
            $this->session->set_userdata('book_import_cache', [
                'questions' => $result['questions'],
                'category_id' => $category_id,
                'subcategory_id' => $subcategory_id,
                'exam_id' => $exam_id,
                'badge' => $badge,
                'title' => $result['title']
            ]);

            return $this->json_response([
                'error' => false,
                'title' => $result['title'],
                'total' => count($result['questions']),
                'preview' => array_slice($result['questions'], 0, 30),
                'message' => count($result['questions']) . ' soru ve çözüm başarıyla analiz edildi.'
            ]);
        }

        // Handle direct PDF URL or Upload
        $filePath = '';
        $docTitle = 'PDF Dokümanı';
        if (!empty($_FILES['pdf_file']['name'])) {
            $docTitle = $_FILES['pdf_file']['name'];
            $tmpPath = $_FILES['pdf_file']['tmp_name'];
            $filePath = sys_get_temp_dir() . '/upload_' . time() . '.pdf';
            move_uploaded_file($tmpPath, $filePath);
        } else if (!empty($url)) {
            $docTitle = basename(parse_url($url, PHP_URL_PATH) ?? 'indirilen_belge.pdf');
            $filePath = sys_get_temp_dir() . '/download_' . time() . '.pdf';
            $ch = curl_init($url);
            $fp = fopen($filePath, 'wb');
            curl_setopt($ch, CURLOPT_FILE, $fp);
            curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
            curl_setopt($ch, CURLOPT_TIMEOUT, 60);
            curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
            curl_exec($ch);
            curl_close($ch);
            fclose($fp);
        }

        if (empty($filePath) || !file_exists($filePath) || filesize($filePath) < 100) {
            echo json_encode(['error' => true, 'message' => 'PDF dosyası indirilemedi veya geçersiz.']);
            return;
        }

        $result = $this->parse_generic_pdf($filePath, $badge);
        @unlink($filePath);

        if ($result['error']) {
            return $this->json_response($result);
        }

        $result['title'] = $docTitle;

        if (empty($result['questions'])) {
            return $this->json_response([
                'error' => true,
                'message' => 'PDF dosyasında soru veya şık formatı tespit edilemedi. Dosya taranmış fotokopi/görsel olabilir.'
            ]);
        }

        $this->session->set_userdata('book_import_cache', [
            'questions' => $result['questions'],
            'category_id' => $category_id,
            'subcategory_id' => $subcategory_id,
            'exam_id' => $exam_id,
            'badge' => $badge,
            'title' => $result['title']
        ]);

        return $this->json_response([
            'error' => false,
            'title' => $result['title'],
            'total' => count($result['questions']),
            'preview' => array_slice($result['questions'], 0, 30),
            'message' => count($result['questions']) . ' soru başarıyla analiz edildi.'
        ]);
    }

    public function save()
    {
        if (!has_permissions('create', 'questions')) {
            return $this->json_response(['error' => true, 'message' => 'Yetkiniz bulunmamaktadır.']);
        }

        $cached = $this->session->userdata('book_import_cache');
        if (empty($cached) || empty($cached['questions'])) {
            return $this->json_response(['error' => true, 'message' => 'Aktarılacak soru bulunamadı. Lütfen önce analiz yapınız.']);
        }

        $category_id = intval($this->input->post('category_id') ?? $cached['category_id']);
        $subcategory_id = intval($this->input->post('subcategory_id') ?? $cached['subcategory_id']);
        $exam_id = intval($this->input->post('exam_id') ?? $cached['exam_id']);
        $badge = trim($this->input->post('badge') ?? $cached['badge']);

        $questions = $cached['questions'];
        $inserted = 0;
        $this->db->trans_start();

        foreach ($questions as $q) {
            $qText = $q['question'];
            if (!empty($badge) && strpos($qText, $badge) === false) {
                $qText = "[$badge]\n\n" . $qText;
            }

            $note = $q['solution'] ?? '';
            if (empty($note) && !empty($q['note'])) {
                $note = $q['note'];
            }

            $finalCat = ($category_id > 0) ? $category_id : (!empty($q['category']) ? intval($q['category']) : 1);
            $finalSub = ($subcategory_id > 0) ? $subcategory_id : (!empty($q['subcategory']) ? intval($q['subcategory']) : 0);

            $insertData = [
                'category' => $finalCat,
                'subcategory' => $finalSub,
                'language_id' => 52, // Turkish
                'image' => '',
                'question' => $qText,
                'question_type' => 1,
                'optiona' => $q['optiona'],
                'optionb' => $q['optionb'],
                'optionc' => $q['optionc'],
                'optiond' => $q['optiond'],
                'optione' => $q['optione'],
                'answer' => strtolower($q['answer']),
                'level' => 1,
                'note' => $note
            ];

            $this->db->insert('tbl_question', $insertData);
            $newQuestionId = $this->db->insert_id();
            $inserted++;

            // Link to Exam Module if selected
            if ($exam_id > 0 && $newQuestionId > 0 && $this->db->table_exists('tbl_exam_module_question')) {
                $this->db->insert('tbl_exam_module_question', [
                    'exam_module_id' => $exam_id,
                    'question_id' => $newQuestionId
                ]);
            }
        }

        $this->db->trans_complete();

        // Clear cache
        $this->session->unset_userdata('book_import_cache');

        return $this->json_response([
            'error' => false,
            'message' => "Toplam $inserted adet soru ve detaylı çözümü başarıyla veritabanına eklendi!",
            'redirect' => base_url('manage-questions')
        ]);
    }

    private function parse_scribd_url($url, $badge)
    {
        // Extract document id
        preg_match('/(?:document|embeds)\/(\d+)/', $url, $m);
        if (empty($m[1])) {
            return ['error' => true, 'message' => 'Scribd belge kimliği (ID) URL içinde bulunamadı.'];
        }
        $docId = $m[1];
        $embedUrl = "https://www.scribd.com/embeds/$docId/content";

        $ch = curl_init($embedUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 15);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
        $html = curl_exec($ch);
        curl_close($ch);

        if (empty($html) || strpos($html, 'Client Challenge') !== false) {
            return [
                'error' => true,
                'is_bot_challenge' => true,
                'doc_id' => $docId,
                'embed_url' => $embedUrl,
                'message' => 'Scribd doğrudan sunucu bağlantısını bot koruması (Kasada Challenge) ile engelledi.'
            ];
        }

        // Title
        preg_match('/<title>(.*?)<\/title>/', $html, $tm);
        $title = !empty($tm[1]) ? str_replace(' | PDF', '', $tm[1]) : 'Scribd Kitap Soru Bankası';

        // Find page URLs
        preg_match_all('/pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"/s', $html, $pageMatches);
        if (empty($pageMatches[1])) {
            return [
                'error' => true,
                'is_bot_challenge' => true,
                'doc_id' => $docId,
                'embed_url' => $embedUrl,
                'message' => 'Scribd sayfa içeriği doğrudan okunamadı (Bot Koruması).'
            ];
        }

        $pageUrls = [];
        foreach ($pageMatches[1] as $idx => $pnum) {
            $pageUrls[intval($pnum)] = $pageMatches[2][$idx];
        }

        $allQuestions = [];
        // Fetch pages and extract
        foreach ($pageUrls as $pnum => $pageUrl) {
            if ($pnum < 5) continue; // skip front cover/toc

            $ch = curl_init($pageUrl);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_TIMEOUT, 6);
            curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0');
            $raw = curl_exec($ch);
            curl_close($ch);

            if (empty($raw)) continue;
            if (substr($raw, 0, 2) === "\x1f\x8b") {
                $raw = @gzdecode($raw);
            }
            if (empty($raw)) continue;

            $pageQuestions = $this->parse_scribd_page_spans($raw, $pnum, $title, $badge);
            foreach ($pageQuestions as $pq) {
                $allQuestions[] = $pq;
            }
        }

        $cleaned = $this->clean_extracted_questions($allQuestions);

        return [
            'error' => false,
            'title' => $title,
            'questions' => $cleaned
        ];
    }

    private function parse_scribd_html_string($html, $badge)
    {
        if (empty($html)) {
            return ['error' => true, 'message' => 'HTML kaynak kodu boş olamaz.'];
        }

        // Title
        preg_match('/<title>(.*?)<\/title>/', $html, $tm);
        $title = !empty($tm[1]) ? str_replace(' | PDF', '', $tm[1]) : 'Scribd Kitap Soru Bankası';

        // Find page URLs via addPage or jsonp urls
        $pageUrls = [];
        preg_match_all('/pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"/s', $html, $pageMatches);
        if (!empty($pageMatches[1])) {
            foreach ($pageMatches[1] as $idx => $pnum) {
                $pageUrls[intval($pnum)] = $pageMatches[2][$idx];
            }
        } else {
            // Fallback: search for direct scribdassets URLs
            preg_match_all('/(https?:\/\/html\.scribdassets\.com\/[^\/]+\/pages\/(\d+)-[a-zA-Z0-9]+\.jsonp)/', $html, $assetMatches);
            if (!empty($assetMatches[1])) {
                foreach ($assetMatches[1] as $idx => $u) {
                    $pnum = intval($assetMatches[2][$idx]);
                    $pageUrls[$pnum] = $u;
                }
            }
        }

        if (empty($pageUrls)) {
            return [
                'error' => true,
                'message' => 'Yapıştırılan HTML kaynağında Scribd sayfa bağlantısı tespit edilemedi. Lütfen Scribd embed sayfasında Ctrl+U yaparak tüm kaynak kodunu kopyaladığınızdan emin olun.'
            ];
        }

        ksort($pageUrls);
        $allQuestions = [];

        foreach ($pageUrls as $pnum => $pageUrl) {
            if ($pnum < 5) continue; // skip cover/toc

            $ch = curl_init($pageUrl);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_TIMEOUT, 6);
            curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0');
            $raw = curl_exec($ch);
            curl_close($ch);

            if (empty($raw)) continue;
            if (substr($raw, 0, 2) === "\x1f\x8b") {
                $raw = @gzdecode($raw);
            }
            if (empty($raw)) continue;

            $pageQuestions = $this->parse_scribd_page_spans($raw, $pnum, $title, $badge);
            foreach ($pageQuestions as $pq) {
                $allQuestions[] = $pq;
            }
        }

        $cleaned = $this->clean_extracted_questions($allQuestions);

        if (empty($cleaned)) {
            return ['error' => true, 'message' => 'Sayfalardan soru ve şık metinleri ayrıştırılamadı.'];
        }

        return [
            'error' => false,
            'title' => $title,
            'questions' => $cleaned
        ];
    }

    private function clean_extracted_questions($questions)
    {
        $cleaned = [];
        foreach ($questions as $q) {
            $q_text = $q['question'] ?? '';
            $opt_a = $q['optiona'] ?? '';
            $opt_b = $q['optionb'] ?? '';
            $opt_c = $q['optionc'] ?? '';
            $opt_d = $q['optiond'] ?? '';
            $opt_e = $q['optione'] ?? '';
            $ans = strtolower(trim($q['answer'] ?? ''));
            $sol = $q['solution'] ?? '';

            // Clean leading numbering from question text
            $q_text = preg_replace('/^\s*\d{1,3}\.\s*/u', '', $q_text);
            $q_text = preg_replace('/[\r\n\t]+/', ' ', $q_text);
            $q_text = preg_replace('/\s+/', ' ', $q_text);
            $q_text = trim($q_text);

            // Clean options
            $opt_a = trim(preg_replace('/\s+/', ' ', $opt_a));
            $opt_b = trim(preg_replace('/\s+/', ' ', $opt_b));
            $opt_c = trim(preg_replace('/\s+/', ' ', $opt_c));
            $opt_d = trim(preg_replace('/\s+/', ' ', $opt_d));
            $opt_e = trim(preg_replace('/\s+/', ' ', $opt_e));

            // Clean solution
            $sol = preg_replace('/\s*(Hakimlik|Hukuk Meslekleri|Akademisi)\s*.*$/iu', '', $sol);
            $sol = preg_replace('/\s+/', ' ', $sol);
            $sol = trim($sol);

            if (!empty($opt_a) && !empty($opt_b) && !empty($opt_c) && !empty($opt_d) && !empty($opt_e) && !empty($ans) && mb_strlen($q_text) > 5) {
                $q['question'] = $q_text;
                $q['optiona'] = $opt_a;
                $q['optionb'] = $opt_b;
                $q['optionc'] = $opt_c;
                $q['optiond'] = $opt_d;
                $q['optione'] = $opt_e;
                $q['answer'] = $ans;
                $q['solution'] = $sol;
                $cleaned[] = $q;
            }
        }
        return $cleaned;
    }

    private function parse_scribd_page_spans($raw, $pnum, $title, $badge)
    {
        // Remove JSONP wrapper around content
        $raw = preg_replace('/^window\.page\d+_callback\s*\(\s*\[\s*"/s', '', $raw);
        $raw = preg_replace('/"\s*\]\s*\)\s*;\s*$/s', '', $raw);

        // Extract spans with coordinates: <span class=a style=\"left:Xpx;top:Ypx;...\">TEXT</span>
        preg_match_all('/<span class=a style=\\\\"left:(\d+)px;top:(\d+)px;([^"]*)\\\\"[^>]*>(.*?)(?=(?:<span class=a style=\\\\"left:|<div class=ff|$))/s', $raw, $matches, PREG_SET_ORDER);
        if (empty($matches)) {
            return [];
        }

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

        // Group into questions based on CEVAP: [A-E]
        $questions = [];
        $currentQ = null;

        foreach ($items as $item) {
            $txt = $item['text'];

            // Skip headers/book names/footers
            if (preg_match('/(Hakimlik|Hukuk Meslekleri|Akademisi|1\.Bölüm|İdare Hukuku|\b\d+\s*$)/iu', $txt) && mb_strlen($txt) < 40) {
                continue;
            }

            // Question start: e.g. "1. Aşağıdakilerden...", "2. ..."
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
                    'answer' => '',
                    'category' => 11,
                    'subcategory' => 0
                ];
                continue;
            }

            if (!$currentQ) continue;

            // Options A) .. E)
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

            // Answer
            if (preg_match('/CEVAP\s*:\s*([A-E])/iu', $txt, $am)) {
                $currentQ['answer'] = strtolower($am[1]);
                continue;
            }

            // ÇÖZÜM or DİKKAT trigger
            if (preg_match('/^(ÇÖZÜM|DİKKAT)/iu', $txt)) {
                $cleanSol = preg_replace('/^(ÇÖZÜM|DİKKAT)\s*[:\-]?\s*/iu', '', $txt);
                if (!empty($cleanSol)) {
                    $currentQ['solution'] .= (empty($currentQ['solution']) ? '' : ' ') . $cleanSol;
                }
                continue;
            }

            // Clean leftover JSON brackets
            $txt = preg_replace('/[\]\)\;\"\s]+$/', '', $txt);
            $txt = trim($txt);
            if (empty($txt)) continue;

            // If we have option E but no answer yet, this is the solution text!
            if (!empty($currentQ['optione']) && empty($currentQ['answer'])) {
                $currentQ['solution'] .= (empty($currentQ['solution']) ? '' : ' ') . $txt;
            } else if (empty($currentQ['optiona'])) {
                // Continuation of question text
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

    private function parse_generic_pdf($filePath, $badge)
    {
        // Extract text via pdftotext with UTF-8 encoding and layout preserving geometry
        $cmd = "pdftotext -enc UTF-8 -layout " . escapeshellarg($filePath) . " -";
        $text = shell_exec($cmd);

        // Check if digital text exists
        $cleanLetters = preg_replace('/[^a-zA-Z0-9\x{00C0}-\x{017F}]+/u', '', $text ?? '');
        if (mb_strlen($cleanLetters) < 50) {
            return [
                'error' => true,
                'is_scanned' => true,
                'message' => 'Yüklediğiniz PDF dosyası taranmış görsel/fotokopi (resim) formatındadır. Dosya içerisinde seçilebilir dijital metin katmanı bulunmadığı için sorular doğrudan okunamamıştır. Lütfen metinleri kopyalanabilen dijital bir PDF veya Scribd kitap linki kullanınız.'
            ];
        }

        // Split into pages by form-feed character
        $pages = array_values(array_filter(explode("\x0c", $text), function($p) {
            return !empty(trim($p));
        }));
        $totalPages = count($pages);

        // Check if this is an official ÖSYM KPSS or GY-GK booklet
        $isOsymKpss = (
            (stripos($text, 'GENEL YETENEK') !== false || stripos($text, 'GY-PS') !== false) &&
            (stripos($text, 'GENEL KÜLTÜR') !== false || stripos($text, 'GK-PS') !== false)
        );

        // Extract year if available (e.g. 2019, 2020, 2024)
        $year = '';
        if (preg_match('/(20\d{2})[-\s]*(?:KPSS|Kamu)/iu', $text, $ym)) {
            $year = $ym[1];
        }

        if ($isOsymKpss) {
            // --- 1. FIND ANSWER KEY PAGE (usually the last page or near the end) ---
            $ansKeys = ['GY' => [], 'GK' => []];
            $ansPageIdx = -1;

            for ($p = $totalPages - 1; $p >= max(0, $totalPages - 3); $p--) {
                $pContent = $pages[$p];
                if (stripos($pContent, 'GENEL YETENEK') !== false && stripos($pContent, 'GENEL KÜLTÜR') !== false) {
                    $lines = explode("\n", $pContent);
                    $foundCount = 0;
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
                                $foundCount++;
                            }
                        }
                    }
                    if ($foundCount > 20) {
                        $ansPageIdx = $p;
                        break;
                    }
                }
            }

            // --- 2. EXTRACT QUESTIONS SECTION BY SECTION ---
            $gy_questions = [];
            $gk_questions = [];

            for ($pno = 0; $pno < $totalPages; $pno++) {
                // Skip the answer sheet page during question parsing
                if ($pno === $ansPageIdx) continue;

                $pText = $pages[$pno];
                if (empty(trim($pText))) continue;

                // Determine active test section: GY vs GK
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
                    // Short line with two numbers e.g. '31.             33.'
                    if (strlen($line) < 70 && preg_match('/\s{15,}/', substr($line, 20, 45), $sgm, PREG_OFFSET_CAPTURE)) {
                        $splitPos = 20 + $sgm[0][1] + intval(strlen($sgm[0][0]) / 2);
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

                    // Skip headers and exam footers
                    $skip = false;
                    foreach (['KPSS', 'GENEL YETENEK TESTİ', 'GENEL KÜLTÜR TESTİ', 'Diğer sayfaya', 'TEST BİTTİ', 'Bu testte', 'Cevaplarınızı', 'ÖSYM'] as $kw) {
                        if (strpos($trim, $kw) !== false && strlen($trim) < 70) {
                            $skip = true;
                            break;
                        }
                    }
                    if ($skip) continue;

                    // Question start: e.g. "1.", "2. ", "57."
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

            // Merge questions: GY 1-60, then GK 1-60
            ksort($gy_questions);
            ksort($gk_questions);
            $allQuestions = [];
            foreach ($gy_questions as $q) {
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
                'questions' => $allQuestions
            ];
        }

        // --- 3. GENERIC PDF PARSER (Single-column or standard question bank) ---
        $answerMap = [];
        $lastPagesText = '';
        for ($p = max(0, $totalPages - 3); $p < $totalPages; $p++) {
            $lastPagesText .= "\n" . ($pages[$p] ?? '');
        }

        if (preg_match_all('/(?:^|\s)(\d{1,3})\s*[\.\-:\)]\s*([A-Ea-e])\b/u', $lastPagesText, $ansMatches)) {
            foreach ($ansMatches[1] as $idx => $qnum) {
                $qnumInt = intval($qnum);
                $ansVal = strtolower($ansMatches[2][$idx]);
                $answerMap[$qnumInt] = $ansVal;
            }
        }

        $lines = explode("\n", $text);
        $questions = [];
        $currentQ = null;

        foreach ($lines as $line) {
            $trim = trim($line);
            if (empty($trim)) continue;

            if (preg_match('/^(?:Sayfa\s+\d+|\d+\s*\/\s*\d+|\b\d+\s*$)/iu', $trim)) continue;

            if (preg_match('/^(?:Soru\s+)?(\d{1,3})\s*[\.\-:]\s+(.*)/iu', $trim, $qm)) {
                if ($currentQ && !empty($currentQ['optiona']) && (!empty($currentQ['optionb']) || !empty($currentQ['optionc']))) {
                    $questions[] = $currentQ;
                }
                $qnum = intval($qm[1]);
                $ans = $answerMap[$qnum] ?? '';
                $currentQ = [
                    'qnum' => $qnum,
                    'question' => $qm[2],
                    'optiona' => '',
                    'optionb' => '',
                    'optionc' => '',
                    'optiond' => '',
                    'optione' => '',
                    'solution' => '',
                    'answer' => $ans
                ];
                continue;
            }

            if (!$currentQ) continue;

            if (preg_match('/^A[\)\.]\s*(.*)/iu', $trim, $om)) {
                $currentQ['optiona'] = $om[1];
                continue;
            }
            if (preg_match('/^B[\)\.]\s*(.*)/iu', $trim, $om)) {
                $currentQ['optionb'] = $om[1];
                continue;
            }
            if (preg_match('/^C[\)\.]\s*(.*)/iu', $trim, $om)) {
                $currentQ['optionc'] = $om[1];
                continue;
            }
            if (preg_match('/^D[\)\.]\s*(.*)/iu', $trim, $om)) {
                $currentQ['optiond'] = $om[1];
                continue;
            }
            if (preg_match('/^E[\)\.]\s*(.*)/iu', $trim, $om)) {
                $currentQ['optione'] = $om[1];
                continue;
            }

            if (preg_match('/(?:DOĞRU\s+)?CEVAP\s*[:\-]\s*([A-E])/iu', $trim, $am)) {
                $currentQ['answer'] = strtolower($am[1]);
                continue;
            }

            if (preg_match('/^(?:ÇÖZÜM|AÇIKLAMA)\s*[:\-]?\s*(.*)/iu', $trim, $sm)) {
                $currentQ['solution'] = (empty($currentQ['solution']) ? '' : ' ') . $sm[1];
                continue;
            }

            if (empty($currentQ['optiona'])) {
                $currentQ['question'] .= ' ' . $trim;
            } else if (!empty($currentQ['optione'])) {
                if (empty($currentQ['solution'])) {
                    $currentQ['optione'] .= ' ' . $trim;
                } else {
                    $currentQ['solution'] .= ' ' . $trim;
                }
            } else if (!empty($currentQ['optiond'])) {
                $currentQ['optiond'] .= ' ' . $trim;
            } else if (!empty($currentQ['optionc'])) {
                $currentQ['optionc'] .= ' ' . $trim;
            } else if (!empty($currentQ['optionb'])) {
                $currentQ['optionb'] .= ' ' . $trim;
            } else if (!empty($currentQ['optiona'])) {
                $currentQ['optiona'] .= ' ' . $trim;
            }
        }

        if ($currentQ && !empty($currentQ['optiona']) && (!empty($currentQ['optionb']) || !empty($currentQ['optionc']))) {
            $questions[] = $currentQ;
        }

        $finalQuestions = [];
        foreach ($questions as $q) {
            if (empty($q['answer'])) {
                $q['answer'] = 'a';
                if (empty($q['solution'])) {
                    $q['solution'] = '[Cevap anahtarı metinde yer almadığı için varsayılan A atanmıştır, lütfen panelden kontrol ediniz.]';
                }
            } else if (empty($q['solution'])) {
                $q['solution'] = "Doğru Cevap: " . strtoupper($q['answer']);
            }
            if (empty($q['optione'])) {
                $q['optione'] = '-';
            }
            $finalQuestions[] = $q;
        }

        if (empty($finalQuestions)) {
            return [
                'error' => true,
                'message' => 'PDF dosyasında standart soru yapısı tespit edilemedi. Dosya taranmış görsel olabilir veya metin düzeni farklı olabilir.'
            ];
        }

        return [
            'error' => false,
            'title' => basename($filePath),
            'questions' => $finalQuestions
        ];
    }
}
