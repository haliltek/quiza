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

    public function preview()
    {
        if (!has_permissions('create', 'questions')) {
            echo json_encode(['error' => true, 'message' => 'Yetkiniz bulunmamaktadır.']);
            return;
        }

        $url = trim($this->input->post('url') ?? '');
        $badge = trim($this->input->post('badge') ?? '');
        $category_id = intval($this->input->post('category_id') ?? 11);
        $subcategory_id = intval($this->input->post('subcategory_id') ?? 0);
        $exam_id = intval($this->input->post('exam_id') ?? 0);
        $html_source = trim($this->input->post('html_source') ?? '');

        // Handle raw HTML source paste
        if (!empty($html_source)) {
            $result = $this->parse_scribd_html_string($html_source, $badge);
            if ($result['error']) {
                echo json_encode($result);
                return;
            }
            $this->session->set_userdata('book_import_cache', [
                'questions' => $result['questions'],
                'category_id' => $category_id,
                'subcategory_id' => $subcategory_id,
                'exam_id' => $exam_id,
                'badge' => $badge,
                'title' => $result['title']
            ]);

            echo json_encode([
                'error' => false,
                'title' => $result['title'],
                'total' => count($result['questions']),
                'preview' => array_slice($result['questions'], 0, 30),
                'message' => count($result['questions']) . ' soru ve çözüm kaynak kodundan başarıyla analiz edildi.'
            ]);
            return;
        }

        if (empty($url) && empty($_FILES['pdf_file']['name'])) {
            echo json_encode(['error' => true, 'message' => 'Lütfen geçerli bir kitap linki (Scribd/PDF) girin veya PDF yükleyin.']);
            return;
        }

        // Handle Scribd URL
        if (!empty($url) && strpos($url, 'scribd.com') !== false) {
            $result = $this->parse_scribd_url($url, $badge);
            if ($result['error']) {
                echo json_encode($result);
                return;
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

            echo json_encode([
                'error' => false,
                'title' => $result['title'],
                'total' => count($result['questions']),
                'preview' => array_slice($result['questions'], 0, 30),
                'message' => count($result['questions']) . ' soru ve çözüm başarıyla analiz edildi.'
            ]);
            return;
        }

        // Handle direct PDF URL or Upload
        $filePath = '';
        if (!empty($_FILES['pdf_file']['name'])) {
            $tmpPath = $_FILES['pdf_file']['tmp_name'];
            $filePath = sys_get_temp_dir() . '/upload_' . time() . '.pdf';
            move_uploaded_file($tmpPath, $filePath);
        } else if (!empty($url)) {
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
            echo json_encode($result);
            return;
        }

        $this->session->set_userdata('book_import_cache', [
            'questions' => $result['questions'],
            'category_id' => $category_id,
            'subcategory_id' => $subcategory_id,
            'exam_id' => $exam_id,
            'badge' => $badge,
            'title' => $result['title']
        ]);

        echo json_encode([
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
            echo json_encode(['error' => true, 'message' => 'Yetkiniz bulunmamaktadır.']);
            return;
        }

        $cached = $this->session->userdata('book_import_cache');
        if (empty($cached) || empty($cached['questions'])) {
            echo json_encode(['error' => true, 'message' => 'Aktarılacak soru bulunamadı. Lütfen önce analiz yapınız.']);
            return;
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

            $insertData = [
                'category' => $category_id > 0 ? $category_id : ($q['category'] ?? 11),
                'subcategory' => $subcategory_id > 0 ? $subcategory_id : ($q['subcategory'] ?? 0),
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

        echo json_encode([
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
        // Extract text via pdftotext
        $cmd = "pdftotext -layout " . escapeshellarg($filePath) . " -";
        $text = shell_exec($cmd);

        if (empty($text)) {
            return ['error' => true, 'message' => 'PDF içeriği metne dönüştürülemedi. Dosya taranmış görsel olabilir.'];
        }

        // Basic generic question extractor
        $lines = explode("\n", $text);
        $questions = [];
        $currentQ = null;

        foreach ($lines as $line) {
            $trim = trim($line);
            if (preg_match('/^(\d{1,3})\.\s+(.*)/', $trim, $qm)) {
                if ($currentQ && !empty($currentQ['optiona']) && !empty($currentQ['answer'])) {
                    $questions[] = $currentQ;
                }
                $currentQ = [
                    'qnum' => intval($qm[1]),
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

            if (preg_match('/^A\)\s*(.*)/i', $trim, $om)) {
                $currentQ['optiona'] = $om[1];
                continue;
            }
            if (preg_match('/^B\)\s*(.*)/i', $trim, $om)) {
                $currentQ['optionb'] = $om[1];
                continue;
            }
            if (preg_match('/^C\)\s*(.*)/i', $trim, $om)) {
                $currentQ['optionc'] = $om[1];
                continue;
            }
            if (preg_match('/^D\)\s*(.*)/i', $trim, $om)) {
                $currentQ['optiond'] = $om[1];
                continue;
            }
            if (preg_match('/^E\)\s*(.*)/i', $trim, $om)) {
                $currentQ['optione'] = $om[1];
                continue;
            }
            if (preg_match('/(?:DOĞRU\s+)?CEVAP\s*:\s*([A-E])/i', $trim, $am)) {
                $currentQ['answer'] = strtolower($am[1]);
                continue;
            }

            if (empty($currentQ['optiona'])) {
                $currentQ['question'] .= ' ' . $trim;
            } else if (!empty($currentQ['optione'])) {
                $currentQ['solution'] .= ' ' . $trim;
            }
        }

        if ($currentQ && !empty($currentQ['optiona']) && !empty($currentQ['answer'])) {
            $questions[] = $currentQ;
        }

        return [
            'error' => false,
            'title' => basename($filePath),
            'questions' => $questions
        ];
    }
}
