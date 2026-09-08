import subprocess

sql = """
SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';

-- A Grubu Hukuk (58) Questions
SET @cat_huk_58 = (SELECT id FROM tbl_category WHERE language_id = 58 AND category_name LIKE 'Hukuk%' LIMIT 1);
SET @sub_huk_58 = (SELECT id FROM tbl_subcategory WHERE language_id = 58 AND maincat_id = @cat_huk_58 LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
VALUES
(@cat_huk_58, @sub_huk_58, 58, '', '1982 Anayasasına göre TBMM genel seçimleri kaç yılda bir Cumhurbaşkanı seçimi ile birlikte yapılır?', 1, '3 yıl', '4 yıl', '5 yıl', '6 yıl', '7 yıl', 'c', '1982 Anayasası m. 77: TBMM ve Cumhurbaşkanlığı seçimleri 5 yılda bir aynı gün yapılır.', 1),
(@cat_huk_58, @sub_huk_58, 58, '', 'Aşağıdakilerden hangisi Anayasa Mahkemesinin görev ve yetkileri arasında yer almaz?', 1, 'Kanunların Anayasaya uygunluğunu denetlemek', 'Bireysel başvuruları karara bağlamak', 'Yüce Divan sıfatıyla yargılama yapmak', 'Siyasi partilerin kapatılması davalarına bakmak', 'Tüzük ve yönetmeliklerin iptal davalarına ilk derece mahkemesi olarak bakmak', 'e', 'Tüzük ve yönetmeliklerin iptali kural olarak Danıştay ve idare mahkemelerinin görev alanındadır.', 1),
(@cat_huk_58, @sub_huk_58, 58, '', 'İdare hukukunda yetki genişliği ilkesi anayasal olarak yalnızca kime veya hangi birime tanınmıştır?', 1, 'Büyükşehir Belediye Başkanına', 'İl Özel İdaresi Genel Sekreterine', 'İl İdaresinin başı olan Valiye', 'Kaymakama', 'Köy Muhtarına', 'c', 'Anayasa m. 126: İllerin idaresi yetki genişliği esasına dayanır. Yetki genişliği sadece valilere tanınmış bir yetkidir.', 1),
(@cat_huk_58, @sub_huk_58, 58, '', 'İktisatta tüketicinin bir maldan tükettiği her ilave birimden elde ettiği ek tatmine ne ad verilir?', 1, 'Toplam fayda', 'Marjinal fayda', 'Ortalama fayda', 'Azalan verim', 'Fırsat maliyeti', 'b', 'Son birimin sağladığı ilave faydaya marjinal fayda denir.', 1),
(@cat_huk_58, @sub_huk_58, 58, '', 'Kamu gelirleri içerisinde yer alan ve devletin kamu hizmeti karşılığında fertlerden aldığı bedele ne ad verilir?', 1, 'Vergi', 'Harç', 'Resim', 'Şerefiye', 'Para cezası', 'b', 'Harç belirli kamu hizmetlerinden (pasaport yargı vb) yararlananlardan alınan bedeldir.', 1);

-- ÖABT (67) Questions
SET @cat_egt_67 = (SELECT id FROM tbl_category WHERE language_id = 67 AND category_name LIKE 'Eğitim%' LIMIT 1);
SET @cat_turk_67 = (SELECT id FROM tbl_category WHERE language_id = 67 AND category_name LIKE 'Türkçe%' LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
VALUES
(@cat_egt_67, 0, 67, '', 'Piaget bilişsel gelişim kuramına göre bir çocuğun nesnelerin göz önünden kaybolduğunda dahi var olmaya devam ettiğini kavraması hangi dönemin temel kazanımıdır?', 1, 'Duyusal-Motor Dönem', 'İşlem Öncesi Dönem', 'Somut İşlemler Dönemi', 'Soyut İşlemler Dönemi', 'Gizil Dönem', 'a', 'Nesne sürekliliği duyusal-motor dönemin (0-2 yaş) sonuna doğru kazanılır.', 1),
(@cat_egt_67, 0, 67, '', 'Öğretim yöntem ve tekniklerinde öğrencilerin gerçek bir yaşam problemini küçük gruplar halinde senaryolar üzerinden çözerek öğrendiği yaklaşım hangisidir?', 1, 'Basamaklı Öğretim', 'Probleme Dayalı Öğrenme', 'Programlı Öğretim', 'Mikro Öğretim', 'Doğrudan Öğretim', 'b', 'Probleme dayalı öğrenme senaryo temelli gerçek hayat sorunlarının çözümüne dayanır.', 1),
(@cat_egt_67, 0, 67, '', 'Bloom yenilenmiş taksonomisine göre en üst düzey bilişsel basamak aşağıdakilerden hangisidir?', 1, 'Hatırlama', 'Uygulama', 'Analiz etme', 'Değerlendirme', 'Yaratma (Sentez)', 'e', 'Yenilenmiş Bloom taksonomisinde en üst basamak Yaratma (Create) düzeyidir.', 1),
(@cat_turk_67, 0, 67, '', 'Türkçede dört temel dil becerisinden anlama (alıcı) boyutunda yer alan beceriler hangi seçenekte birlikte verilmiştir?', 1, 'Okuma - Dinleme', 'Konuşma - Yazma', 'Okuma - Yazma', 'Dinleme - Konuşma', 'Görsel Okuma - Yazma', 'a', 'Okuma ve Dinleme alıcı/anlama; Konuşma ve Yazma ise anlatma becerileridir.', 1);

-- DHBT (68) Questions
SET @cat_dhbt_68 = (SELECT id FROM tbl_category WHERE language_id = 68 AND category_name LIKE 'DHBT-1%' LIMIT 1);
SET @cat_fik_68 = (SELECT id FROM tbl_category WHERE language_id = 68 AND category_name LIKE 'Fıkıh%' LIMIT 1);

INSERT INTO tbl_question (category, subcategory, language_id, image, question, question_type, optiona, optionb, optionc, optiond, optione, answer, note, level)
VALUES
(@cat_dhbt_68, 0, 68, '', 'Kuran-ı Kerimin ilk indirilen ayetleri hangi surenin başında yer almaktadır?', 1, 'Fatiha Suresi', 'Alak Suresi', 'Müddessir Suresi', 'Bakara Suresi', 'Kadir Suresi', 'b', 'İlk vahiy Alak Suresinin ilk 5 ayetidir.', 1),
(@cat_dhbt_68, 0, 68, '', 'Hz. Muhammedin (s.a.v.) sözleri fiilleri ve takrirlerinden oluşan kaynak İslam hukukunda hangisidir?', 1, 'İcma', 'Kıyas', 'Sünnet', 'İstihsan', 'Maslahat', 'c', 'Hz Peygamberin söz fiil ve onayları Sünnet olarak adlandırılır.', 1),
(@cat_fik_68, 0, 68, '', 'Fıkıhta namazın farzlarından olup namazın dışındaki şartlar (hazırlık şartları) arasında hangisi yer alır?', 1, 'İftitah Tekbiri', 'Kıyam', 'Kıraat', 'Hadesten Taharet', 'Rükû', 'd', 'Hadesten taharet namazın dışındaki hazırlık şartlarındandır diğerleri rükünlerdir.', 1),
(@cat_dhbt_68, 0, 68, '', 'İslam tarihinde Müslümanların ilk hicret ettikleri yer neresidir?', 1, 'Medine (Yesrib)', 'Habeşistan', 'Taif', 'Yemen', 'Şam', 'b', 'İlk hicret Mekkeli müşriklerin baskısı üzerine Habeşistana yapılmıştır.', 1);
"""

cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db --default-character-set=utf8mb4']
res = subprocess.run(cmd, input=sql.encode('utf-8'), capture_output=True)
print("STDOUT:", res.stdout.decode('utf-8', errors='replace'))
print("STDERR:", res.stderr.decode('utf-8', errors='replace'))
print("EXIT CODE:", res.returncode)
