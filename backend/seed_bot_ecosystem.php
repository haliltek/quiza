<?php
/**
 * Quiza Bot Ekosistemi, Sınav Sonuçları ve Puan Dengeleme Scripti
 */

$host = 'elitequiz_db';
$user = 'elite_user';
$pass = 'elite_user_pass_2026';
$db   = 'elite_quiz_db';

$mysqli = new mysqli($host, $user, $pass, $db);
if ($mysqli->connect_errno) {
    die("Veritabanı bağlantı hatası: " . $mysqli->connect_error . "\n");
}
$mysqli->set_charset("utf8mb4");

echo "=== 1. EKONOMİ & PUAN AYARLARININ GÜNCELLENMESİ ===\n";

$settings = [
    'welcome_bonus_coin' => '100', // 100 puan/jeton hediye
    'earn_coin' => '5',            // Video/reklam başına makul jeton
    'refer_coin' => '10',          // Referans başına dengeli jeton
    'battle_mode_group_correct_answer_credit_score' => '4',
    'battle_mode_group_wrong_answer_deduct_score' => '2',
    'battle_mode_group_quickest_correct_answer_extra_score' => '2',
    'battle_mode_group_second_quickest_correct_answer_extra_score' => '1',
    'multi_match_correct_answer_credit_score' => '4',
    'multi_match_wrong_answer_deduct_score' => '2',
    'battle_mode_random_search_duration' => '5', // 5 saniyede otomatik bot eşleşmesi
];

$stmt = $mysqli->prepare("UPDATE tbl_settings SET message = ? WHERE type = ?");
foreach ($settings as $type => $val) {
    $stmt->bind_param("ss", $val, $type);
    $stmt->execute();
    echo "  [Ayar] $type -> $val\n";
}
$stmt->close();

echo "\n=== 2. MEVCUT HALİL HESABININ KALİBRE EDİLMESİ ===\n";
// Halil kullanıcısının şişen puanını (4242) ve jetonunu (4960) dengeli hale getirelim
$mysqli->query("UPDATE tbl_users SET coins = 120 WHERE id = 1");
$mysqli->query("UPDATE tbl_leaderboard_monthly SET score = 140 WHERE user_id = 1");
$mysqli->query("UPDATE tbl_leaderboard_daily SET score = 140 WHERE user_id = 1");
echo "  Halil kullanıcısı güncellendi: 120 Jeton, 140 Puan.\n";

echo "\n=== 3. GERÇEKÇİ BOT KULLANICI HAVUZUNUN OLUŞTURULMASI ===\n";

$botNames = [
    ['Ahmet Yılmaz', 'ahmet.yilmaz@quiza.app', 'male', '1.svg'],
    ['Elif Demir', 'elif.demir@quiza.app', 'female', '2.svg'],
    ['Merve Kaya', 'merve.kaya@quiza.app', 'female', '3.svg'],
    ['Burak Şahin', 'burak.sahin@quiza.app', 'male', '4.svg'],
    ['Zeynep Çelik', 'zeynep.celik@quiza.app', 'female', '5.svg'],
    ['Oğuzhan Koç', 'oguzhan.koc@quiza.app', 'male', '6.svg'],
    ['Fatma Yıldız', 'fatma.yildiz@quiza.app', 'female', '7.svg'],
    ['Emre Arslan', 'emre.arslan@quiza.app', 'male', '8.svg'],
    ['Selin Aydın', 'selin.aydin@quiza.app', 'female', '9.svg'],
    ['Caner Özkan', 'caner.ozkan@quiza.app', 'male', '10.svg'],
    ['Büşra Yıldırım', 'busra.yildirim@quiza.app', 'female', '2.svg'],
    ['Deniz Aktaş', 'deniz.aktas@quiza.app', 'male', '1.svg'],
    ['Gamze Polat', 'gamze.polat@quiza.app', 'female', '3.svg'],
    ['Serkan Kılıç', 'serkan.kilic@quiza.app', 'male', '4.svg'],
    ['Ebru Bozkurt', 'ebru.bozkurt@quiza.app', 'female', '5.svg'],
    ['Mustafa Öztürk', 'mustafa.ozturk@quiza.app', 'male', '6.svg'],
    ['Ayşe Korkmaz', 'ayse.korkmaz@quiza.app', 'female', '7.svg'],
    ['Tolga Güneş', 'tolga.gunes@quiza.app', 'male', '8.svg'],
    ['Hilal Yavuz', 'hilal.yavuz@quiza.app', 'female', '9.svg'],
    ['Yusuf Karaca', 'yusuf.karaca@quiza.app', 'male', '10.svg'],
    ['Eren Doğan', 'eren.dogan@quiza.app', 'male', '1.svg'],
    ['Seda Çetin', 'seda.cetin@quiza.app', 'female', '2.svg'],
    ['Berkant Şen', 'berkant.sen@quiza.app', 'male', '4.svg'],
    ['Melis Kurt', 'melis.kurt@quiza.app', 'female', '3.svg'],
    ['Onur Vural', 'onur.vural@quiza.app', 'male', '6.svg'],
    ['Yasemin Keskin', 'yasemin.keskin@quiza.app', 'female', '5.svg'],
    ['Barış Güler', 'baris.guler@quiza.app', 'male', '8.svg'],
    ['Esra Aslan', 'esra.aslan@quiza.app', 'female', '7.svg'],
    ['Kerem Erdem', 'kerem.erdem@quiza.app', 'male', '10.svg'],
    ['Derya Tunç', 'derya.tunc@quiza.app', 'female', '9.svg'],
    ['Hakan Kaplan', 'hakan.kaplan@quiza.app', 'male', '1.svg'],
    ['Tuğba Tekin', 'tugba.tekin@quiza.app', 'female', '2.svg'],
    ['Umut Yaman', 'umut.yaman@quiza.app', 'male', '4.svg'],
    ['Sinem Çakır', 'sinem.cakir@quiza.app', 'female', '3.svg'],
    ['Furkan Sarı', 'furkan.sari@quiza.app', 'male', '6.svg'],
    ['İpek Tan', 'ipek.tan@quiza.app', 'female', '5.svg'],
    ['Cihan Bulut', 'cihan.bulut@quiza.app', 'male', '8.svg'],
    ['Gökçe Ünal', 'gokce.unal@quiza.app', 'female', '7.svg'],
    ['Tayfun Koçak', 'tayfun.kocak@quiza.app', 'male', '10.svg'],
    ['Ezgi Taş', 'ezgi.tas@quiza.app', 'female', '9.svg'],
    ['Murat Yalçın', 'murat.yalcin@quiza.app', 'male', '1.svg'],
    ['Sevgi Avcı', 'sevgi.avci@quiza.app', 'female', '2.svg'],
    ['Alper Yıldız', 'alper.yildiz@quiza.app', 'male', '4.svg'],
    ['Nazlı Parlak', 'nazli.parlak@quiza.app', 'female', '3.svg'],
    ['Volkan Aydın', 'volkan.aydin@quiza.app', 'male', '6.svg'],
    ['Pınar Özdemir', 'pinar.ozdemir@quiza.app', 'female', '5.svg'],
    ['Burcu Turan', 'burcu.turan@quiza.app', 'female', '7.svg'],
    ['Koray Özer', 'koray.ozer@quiza.app', 'male', '8.svg'],
    ['Duygu Dinçer', 'duygu.dincer@quiza.app', 'female', '9.svg'],
    ['Kaan Aksoy', 'kaan.aksoy@quiza.app', 'male', '10.svg'],
    ['Gizem Taşkın', 'gizem.taskin@quiza.app', 'female', '2.svg'],
    ['Mert Çakmak', 'mert.cakmak@quiza.app', 'male', '1.svg'],
    ['Sibel Güven', 'sibel.guven@quiza.app', 'female', '3.svg'],
    ['Cem Karadağ', 'cem.karadag@quiza.app', 'male', '4.svg'],
    ['Beyza Öztürk', 'beyza.ozturk@quiza.app', 'female', '5.svg']
];

$botUserIds = [];

$checkUserStmt = $mysqli->prepare("SELECT id FROM tbl_users WHERE email = ?");
$insertUserStmt = $mysqli->prepare("INSERT INTO tbl_users (firebase_id, name, email, mobile, type, profile, coins, status, date_registered, api_token) VALUES (?, ?, ?, ?, 'email', ?, ?, 1, ?, ?)");

foreach ($botNames as $idx => $b) {
    $name = $b[0];
    $email = $b[1];
    $avatar = $b[3];
    
    $checkUserStmt->bind_param("s", $email);
    $checkUserStmt->execute();
    $res = $checkUserStmt->get_result();
    
    if ($row = $res->fetch_assoc()) {
        $uId = $row['id'];
        // Profil ve isim güncellemesi
        $updateStmt = $mysqli->prepare("UPDATE tbl_users SET name = ?, profile = ? WHERE id = ?");
        $updateStmt->bind_param("ssi", $name, $avatar, $uId);
        $updateStmt->execute();
        $updateStmt->close();
    } else {
        $firebaseId = 'bot_fb_' . md5($email);
        $mobile = '5' . rand(30, 55) . rand(1000000, 9999999);
        $coins = rand(80, 250);
        $regDate = date('Y-m-d H:i:s', strtotime('-' . rand(2, 45) . ' days'));
        $apiToken = 'bot_token_' . md5($firebaseId . $regDate);
        
        $insertUserStmt->bind_param("sssssiss", $firebaseId, $name, $email, $mobile, $avatar, $coins, $regDate, $apiToken);
        $insertUserStmt->execute();
        $uId = $insertUserStmt->insert_id;
    }
    $botUserIds[] = $uId;
}
$checkUserStmt->close();
$insertUserStmt->close();

echo "  Toplam " . count($botUserIds) . " bot kullanıcı hazırlandı.\n";

echo "\n=== 4. HEDEF SINAV KATILIMLARININ OLUŞTURULMASI (tbl_exam_module_result) ===\n";

// Mevcut sınavları çekelim
$examsRes = $mysqli->query("SELECT id, title, duration FROM tbl_exam_module WHERE status = 1");
$exams = [];
while ($row = $examsRes->fetch_assoc()) {
    $exams[] = $row;
}

// Önce eski bot sınav sonuçlarını temizleyelim (varsa)
$mysqli->query("TRUNCATE TABLE tbl_exam_module_result");

$insertExamResult = $mysqli->prepare("INSERT INTO tbl_exam_module_result (exam_module_id, user_id, obtained_marks, total_duration, statistics, status, rules_violated, captured_question_ids) VALUES (?, ?, ?, ?, ?, 3, 0, '')");

foreach ($exams as $exam) {
    $examId = $exam['id'];
    $examTitle = $exam['title'];
    $maxDuration = (int)$exam['duration'] * 60; // saniyeye çevir
    
    // Sınavdaki soru sayısı ve toplam puanı öğrenelim
    $qRes = $mysqli->query("SELECT COUNT(*) as q_count, marks FROM tbl_exam_module_question WHERE exam_module_id = $examId GROUP BY marks");
    $qRow = $qRes->fetch_assoc();
    $totalQuestions = $qRow ? (int)$qRow['q_count'] : 20;
    $markPerQuestion = $qRow ? (int)$qRow['marks'] : 5;
    $maxScore = $totalQuestions * $markPerQuestion;
    
    // Her sınav için 32-42 arası rastgele bot seçelim
    $participantCount = rand(32, 42);
    $selectedBots = $botUserIds;
    shuffle($selectedBots);
    $participants = array_slice($selectedBots, 0, $participantCount);
    
    echo "  Sınav ID $examId ($examTitle): $participantCount katılımcı işleniyor...\n";
    
    foreach ($participants as $pUserId) {
        // Çan eğrisi / Gerçekçi başarı oranı: %35 ile %95 arası
        // %15 üst grup (yüksek puan), %70 orta grup, %15 alt grup
        $randRoll = rand(1, 100);
        if ($randRoll <= 15) {
            // Yüksek başarı (%85 - %100)
            $correctRatio = rand(85, 100) / 100.0;
        } elseif ($randRoll <= 85) {
            // Orta grup (%60 - %84)
            $correctRatio = rand(60, 84) / 100.0;
        } else {
            // Düşük grup (%30 - %59)
            $correctRatio = rand(30, 59) / 100.0;
        }
        
        $correctAnswers = round($totalQuestions * $correctRatio);
        if ($correctAnswers > $totalQuestions) $correctAnswers = $totalQuestions;
        $incorrectAnswers = $totalQuestions - $correctAnswers;
        $obtainedMarks = (string)($correctAnswers * $markPerQuestion);
        
        // Gerçekçi süre: Soru başına ortalama 15-35 saniye
        $durationSeconds = rand((int)($totalQuestions * 15), (int)($totalQuestions * 35));
        if ($durationSeconds > $maxDuration) $durationSeconds = $maxDuration - rand(10, 60);
        $totalDurationStr = (string)$durationSeconds;
        
        $stats = [
            [
                "mark" => (string)$markPerQuestion,
                "correct_answer" => (string)$correctAnswers,
                "incorrect" => (string)$incorrectAnswers
            ]
        ];
        $statsJson = json_encode($stats);
        
        $insertExamResult->bind_param("iisss", $examId, $pUserId, $obtainedMarks, $totalDurationStr, $statsJson);
        $insertExamResult->execute();
    }
}
$insertExamResult->close();
echo "  Tüm hedef sınavlara en az 30-40 gerçekçi sınav sonucu eklendi.\n";

echo "\n=== 5. LİDERLİK TABLOLARININ (tbl_leaderboard_daily & monthly) GÜNCELLENMESİ ===\n";

// Eski şişmiş skorları temizleyelim
$mysqli->query("TRUNCATE TABLE tbl_leaderboard_daily");
$mysqli->query("TRUNCATE TABLE tbl_leaderboard_monthly");

$insertMonthly = $mysqli->prepare("INSERT INTO tbl_leaderboard_monthly (user_id, score, last_updated, date_created) VALUES (?, ?, NOW(), NOW())");
$insertDaily = $mysqli->prepare("INSERT INTO tbl_leaderboard_daily (user_id, score, date_created) VALUES (?, ?, NOW())");

// Halil'i liderlik tablosuna dengeli puanla yerleştirelim
$halilId = 1;
$halilScore = 140;
$insertMonthly->bind_param("ii", $halilId, $halilScore);
$insertMonthly->execute();
$insertDaily->bind_param("ii", $halilId, $halilScore);
$insertDaily->execute();

// Botları gerçekçi aylık ve günlük skor dağılımına yerleştirelim
// Aylık skorlar: 80 - 750 puan arası
// Günlük skorlar: 15 - 160 puan arası
$shuffledBots = $botUserIds;
shuffle($shuffledBots);

// En iyi ilk 5 bot (180 - 280 aylık puan)
$tier1 = array_slice($shuffledBots, 0, 5);
// Orta grup 20 bot (90 - 170 aylık puan)
$tier2 = array_slice($shuffledBots, 5, 20);
// Başlangıç grubu 20 bot (30 - 85 aylık puan)
$tier3 = array_slice($shuffledBots, 25, 20);

$monthlyScores = [];
$dailyScores = [];

foreach ($tier1 as $bId) {
    $mScore = rand(220, 320);
    $dScore = rand(40, 80);
    $monthlyScores[$bId] = $mScore;
    $dailyScores[$bId] = $dScore;
}
foreach ($tier2 as $bId) {
    $mScore = rand(100, 210);
    $dScore = rand(20, 45);
    $monthlyScores[$bId] = $mScore;
    $dailyScores[$bId] = $dScore;
}
foreach ($tier3 as $bId) {
    $mScore = rand(30, 95);
    $dScore = rand(8, 25);
    $monthlyScores[$bId] = $mScore;
    $dailyScores[$bId] = $dScore;
}

foreach ($monthlyScores as $bId => $mScore) {
    $insertMonthly->bind_param("ii", $bId, $mScore);
    $insertMonthly->execute();
}
foreach ($dailyScores as $bId => $dScore) {
    $insertDaily->bind_param("ii", $bId, $dScore);
    $insertDaily->execute();
}

$insertMonthly->close();
$insertDaily->close();

echo "  Liderlik tabloları dengeli ve organik puanlarla dolduruldu.\n";

echo "\n=== 6. KULLANICI İSTATİSTİKLERİ & DÜELLO GEÇMİŞİ ===\n";

$mysqli->query("TRUNCATE TABLE tbl_users_statistics");
$insertStat = $mysqli->prepare("INSERT INTO tbl_users_statistics (user_id, questions_answered, correct_answers, strong_category, ratio1, weak_category, ratio2, best_position, date_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NOW())");

// Halil için başlangıç istatistiği
$hAnswered = 35; $hCorrect = 28; $hStrong = 1; $hRatio1 = 80; $hWeak = 2; $hRatio2 = 20; $hBest = 12;
$insertStat->bind_param("iiisiiii", $halilId, $hAnswered, $hCorrect, $hStrong, $hRatio1, $hWeak, $hRatio2, $hBest);
$insertStat->execute();

$rankIndex = 1;
foreach ($botUserIds as $bId) {
    $answered = rand(40, 180);
    // %70-%85 arası doğruluk
    $accuracy = rand(70, 85) / 100.0;
    $correct = round($answered * $accuracy);
    $strongCat = rand(1, 4);
    $weakCat = rand(1, 4);
    $r1 = rand(70, 90);
    $r2 = 100 - $r1;
    $bestPos = $rankIndex++;
    
    $insertStat->bind_param("iiisiiii", $bId, $answered, $correct, $strongCat, $r1, $weakCat, $r2, $bestPos);
    $insertStat->execute();
}
$insertStat->close();

// Düello istatistikleri (tbl_battle_statistics)
$mysqli->query("TRUNCATE TABLE tbl_battle_statistics");
$insertBattle = $mysqli->prepare("INSERT INTO tbl_battle_statistics (user_id1, user_id2, is_drawn, winner_id, date_created) VALUES (?, ?, ?, ?, NOW())");

for ($i = 0; $i < 60; $i++) {
    $u1 = $botUserIds[array_rand($botUserIds)];
    $u2 = $botUserIds[array_rand($botUserIds)];
    if ($u1 == $u2) continue;
    
    $isDrawn = (rand(1, 10) == 1) ? 1 : 0;
    $winner = $isDrawn ? 0 : ((rand(1, 2) == 1) ? $u1 : $u2);
    
    $insertBattle->bind_param("iiii", $u1, $u2, $isDrawn, $winner);
    $insertBattle->execute();
}
$insertBattle->close();
echo "  Kullanıcı istatistikleri ve düello geçmişleri başarıyla kaydedildi.\n";

$mysqli->close();
echo "\n=== TÜM VERİTABANI İŞLEMLERİ BAŞARIYLA TAMAMLANDI! ===\n";
