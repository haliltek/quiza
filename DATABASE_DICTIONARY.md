# Quiza (Elite Quiz v2.3.9.1) — Veritabanı Veri Sözlüğü (Database Dictionary)

Bu belge, **Quiza (Elite Quiz v2.3.9.1)** MySQL 8.0 veritabanındaki (`elite_quiz_db`) temel tabloları, sütun yapılarını, indeksleri ve veri ilişkilerini açıklamaktadır.

---

## 1. Veritabanı Genel Bilgileri

- **Veritabanı Adı:** `elite_quiz_db`
- **Karakter Seti (Charset):** `utf8mb4`
- **Karşılaştırma (Collation):** `utf8mb4_unicode_ci`
- **Depolama Motoru:** InnoDB
- **Toplam Tablo Sayısı:** 56

---

## 2. Temel Tablolar ve Veri Modeli

### A. Kimlik Doğrulama ve Yönetici Tabloları

#### `tbl_authenticate`
Yönetim paneli yöneticileri, moderatörler ve yetkilendirme rolleri.
- `auth_id` (INT, PK, AUTO_INCREMENT): Yönetici tekil ID'si.
- `auth_username` (VARCHAR): Giriş kullanıcı adı.
- `auth_pass` (VARCHAR): Bcrypt ile şifrelenmiş parola hash'i.
- `role` (VARCHAR): Kullanıcı rolü (`admin`, `editor`).
- `permissions` (TEXT): İzin verilen modüllerin JSON haritası.
- `status` (TINYINT): Hesap durumu (1: Aktif, 0: Pasif).

#### `tbl_users`
Mobil ve web uygulamasında kayıt olan son kullanıcılar.
- `id` (INT, PK, AUTO_INCREMENT): Kullanıcı ID.
- `firebase_id` (VARCHAR): Firebase Auth tekil kullanıcı kimliği.
- `name` (VARCHAR): Kullanıcı adı / görünen ad.
- `email` (VARCHAR): E-posta adresi.
- `mobile` (VARCHAR): Telefon numarası.
- `type` (VARCHAR): Giriş tipi (`email`, `gmail`, `phone`, `apple`).
- `profile` (TEXT): Profil avatar URL veya dosya yolu.
- `coins` (INT): Mevcut jeton bakiyesi.
- `status` (TINYINT): Hesap durumu (1: Aktif, 0: Engelli).
- `refer_code` (VARCHAR): Kullanıcının davet kodu.
- `friends_code` (VARCHAR): Kullanıcının kayıt olurken kullandığı referans kodu.

---

### B. Soru Bankası ve Kategori Tabloları

#### `tbl_category`
Ana kategoriler (örn: Bilim, Tarih, Spor, Coğrafya).
- `id` (INT, PK, AUTO_INCREMENT)
- `category_name` (VARCHAR): Kategori başlığı.
- `image` (VARCHAR): Kategori kapak görseli.
- `language_id` (INT): Bağlı olduğu dil ID (`tbl_languages`).
- `row_order` (INT): Sıralama önceliği.

#### `tbl_subcategory`
Alt kategoriler (örn: Bilim -> Fizik, Kimya, Biyoloji).
- `id` (INT, PK, AUTO_INCREMENT)
- `maincat_id` (INT): Ana kategori ID (`tbl_category.id`).
- `subcategory_name` (VARCHAR): Alt kategori adı.
- `status` (TINYINT): 1: Aktif, 0: Pasif.

#### `tbl_question`
Standart sınav modu soruları (Quiz Zone).
- `id` (INT, PK, AUTO_INCREMENT)
- `category` (INT): Kategori ID.
- `subcategory` (INT): Alt kategori ID (varsa).
- `language_id` (INT): Dil ID.
- `image` (VARCHAR): Varsa soru görseli.
- `question` (TEXT): Soru metni.
- `question_type` (TINYINT): 1: Standart şıklı, 2: Doğru/Yanlış.
- `optiona`, `optionb`, `optionc`, `optiond`, `optione` (TEXT): Şık metinleri.
- `answer` (VARCHAR): Doğru şık (`a`, `b`, `c`, `d`, `e`).
- `note` (TEXT): Soru çözüm açıklaması (Cevap sonrası gösterilir).
- `level` (INT): Sorunun ait olduğu zorluk seviyesi.

#### `tbl_ai_questions` (v2.3.9 Yeni)
Yapay zeka motoru tarafından otomatik üretilen soru havuzu.
- `id` (INT, PK, AUTO_INCREMENT)
- `category_id` (INT): Atanan kategori.
- `subcategory_id` (INT): Atanan alt kategori.
- `language_id` (INT): Dil.
- `question` (TEXT): Üretilen soru.
- `optiona`, `optionb`, `optionc`, `optiond` (TEXT): Üretilen seçenekler.
- `answer` (VARCHAR): Doğru cevap.
- `status` (TINYINT): Onay durumu (0: Taslak, 1: Onaylandı/Aktarıldı).

---

### C. Oyun ve Yarışma Modülleri

#### `tbl_contest`
Ödüllü yarışmalar / turnuvalar.
- `id` (INT, PK, AUTO_INCREMENT)
- `name` (VARCHAR): Yarışma adı.
- `start_date` / `end_date` (DATETIME): Yarışmanın geçerlilik tarihleri.
- `entry` (INT): Katılım için gereken jeton miktarı.
- `top_users` (INT): Ödül verilecek ilk N kullanıcı sayısı.

#### `tbl_daily_quiz`
Her takvim gününe özel tanımlanan sınav soruları.
- `id` (INT, PK, AUTO_INCREMENT)
- `date_published` (DATE): Sorunun yayınlanacağı takvim günü.
- `questions_id` (TEXT): Günün sorularının virgülle ayrılmış ID listesi.

#### `tbl_battle_statistics` & `tbl_rooms`
1v1 ve Grup savaşları istatistikleri ve oda geçmişi.

---

### D. Sistem ve Finans Tabloları

#### `tbl_settings`
Sistem genel ayarları, API anahtarları, Firebase parametreleri ve metin şablonları.
- `type` (VARCHAR, KEY): Ayar anahtarı (`system_configurations`, `contact_us`, `terms`, vb.).
- `message` (LONGTEXT): Ayar içeriği veya JSON veri bloğu.

#### `tbl_badges` & `tbl_users_badges`
Kazanılabilir rozetler ve kullanıcıların kazandığı rozet eşleşmeleri.

#### `tbl_payment_request`
Kullanıcıların jetonlarını çekmek için oluşturdukları para çekme talepleri.
- `id` (INT, PK, AUTO_INCREMENT)
- `uid` (INT): Kullanıcı ID.
- `payment_address` (TEXT): IBAN / Papara / Kripto veya PayPal ödeme adresi.
- `request_type` (VARCHAR): Ödeme yöntemi.
- `request_amount` (DOUBLE): Talep edilen tutar.
- `coin_used` (INT): Harcanan jeton.
- `status` (TINYINT): 0: Bekliyor, 1: Ödendi, 2: Reddedildi.
