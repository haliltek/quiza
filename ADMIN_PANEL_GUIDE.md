# Quiza (Elite Quiz v2.3.9.1) — Yönetim Paneli & API Rehberi (Admin Panel Guide)

Bu kılavuz, **Quiza (Elite Quiz v2.3.9.1)** yönetim panelinin (`Admin Panel`) tüm modüllerini, yapılandırma adımlarını, v2.3.9 sürümüyle gelen yeni yapay zeka özelliklerini ve RESTful API uç noktalarını açıklamaktadır.

---

## 1. Yönetim Paneline Erişim

- **Canlı Panel URL:** `http://142.93.104.78:8088`
- **Varsayılan Kullanıcı Adı:** `admin`
- **Varsayılan Şifre:** `admin123`

> [!IMPORTANT]
> İlk girişin ardından **Profile** menüsünden şifrenizi güncellemeniz ve Firebase servis hesabınızı (`serviceAccountKey.json`) yüklemeniz önerilir.

---

## 2. Temel Modüller ve Yetenek Haritası

Yönetim paneli 8 ana operasyonel bölümden oluşur:

### A. Soru Bankası ve Kategori Yönetimi
- **Kategoriler (`Categories`):** Ana kategorilerin oluşturulması, simge/görsel atanması ve dil bazlı filtrelenmesi.
- **Alt Kategoriler (`Subcategories`):** Ana kategorilere bağlı alt dalların tanımlanması.
- **Soru Yönetimi (`Manage Questions`):**
  - Çoktan seçmeli sorular (4 veya 5 seçenekli - Option E desteği).
  - Doğru/Yanlış soruları (`True/False`).
  - Matematik soruları (`Math Quiz` - LaTeX formül desteği).
  - Sesli sorular (`Audio Questions` - MP3 yükleme ve dinleyerek cevaplama).
  - Görselli sorular (Resimli soru ve şıklar).
- **Toplu İçe Aktarma (`Bulk Import`):** CSV veya Excel formatında binlerce sorunun tek tıkla sisteme aktarılması.

### B. v2.3.9 Yeni Özellik: Yapay Zeka ile Soru Üretimi (AI Questions)
Yönetim panelinde yer alan **AI Settings** menüsü üzerinden yapay zeka sağlayıcınızı bağlayabilirsiniz:
1. **Sağlayıcı Seçenekleri:**
   - **Google Gemini:** `gemini-1.5-flash`, `gemini-1.5-pro` (Önerilen, hızlı ve düşük maliyetli).
   - **OpenAI:** `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`.
2. **Kullanım:**
   - Kategori, zorluk seviyesi ve soru adedi seçilir.
   - Yapay zeka, belirlenen konuda soru metnini, doğru cevabı ve 3 yanıltıcı şıkkı otomatik üretir.
   - İnceleme ekranından onaylanan sorular tek tıkla soru bankasına aktarılır.

### C. Oyun ve Yarışma Modları
- **Quiz Zone:** Seviyeli ilerleme (Level-based progression).
- **1v1 Battle:** İki oyuncunun rastgele veya oda kodu ile canlı düellosu.
- **Group Battle:** 4 kişiye kadar arkadaş grubuyla yarışma.
- **Daily Quiz:** Her güne özel belirlenen günlük soru seti.
- **Contest (Ödüllü Yarışmalar):** Belirli tarih/saat aralığında düzenlenen, giriş ücretli ve jeton ödüllü turnuvalar.
- **Guess The Word:** Harf tahmin ederek kelime bulma oyunu.
- **Fun 'N' Learn:** Kısa bilgilendirici bir metin okutulup ardından metinle ilgili soruların sorulduğu öğrenme modu.
- **Self Challenge:** Kullanıcının kendi kategori, soru adedi ve süresini belirlediği pratik modu.
- **Exam Module:** Süreli ve resmi sınav formatında test çözümü.

### D. Rozetler ve Başarı Sistemi (Badges)
Kullanıcı motivasyonunu artıran dinamik rozetler:
- *Dashing Debut* (İlk oyununu oynayan)
- *Combat Winner* (1v1 düello kazanan)
- *Quiz Warrior* (100+ soru çözen)
- *Super Sonic* (Saniyeler içinde doğru cevaplayan)
- *Streak Master* (Kesintisiz her gün giriş yapan)

### E. Para Kazanma & Ödül Sistemi (Monetization & Wallet)
- **Coin Store:** Uygulama içi satın alma (IAP) ile jeton satışı.
- **Reward Ads:** Reklam izleyerek ipucu/jeton kazanma.
- **Ödül Talepleri (`Payment Requests`):** Kullanıcıların topladıkları jetonları gerçek paraya dönüştürme taleplerinin onay/ret yönetimi.

---

## 3. Sistem Yapılandırması (System Configurations)

`System Configurations` menüsü üzerinden tüm ekosistemin davranışları anlık olarak yönetilir:

| Parametre | Varsayılan | Açıklama |
|---|---|---|
| `system_timezone` | `Asia/Kolkata` -> `Europe/Istanbul` | Sistem zaman dilimi |
| `language_mode` | `1` (Aktif) | Çoklu dil desteğini açar/kapatır |
| `option_e_mode` | `1` (Aktif) | 5. şıkkın (E seçeneği) görünürlüğü |
| `daily_quiz_mode` | `1` (Aktif) | Günlük sınav özelliğini açar |
| `in_app_purchase_mode` | `1` (Aktif) | Jeton mağazasını açar |
| `force_update` | `0` (Kapalı) | Mağazadaki yeni sürümü zorunlu kılar |
| `app_version` | `1.0.0+1` | Zorunlu güncelleme sürüm kontrolü |

---

## 4. RESTful API Referansı

Mobil ve Web uygulamaları, yönetim panelinin REST API katmanı ile haberleşir:
- **Temel URL:** `http://142.93.104.78:8088/api/`
- **İstek Formatı:** HTTP POST (`multipart/form-data` veya `application/x-www-form-urlencoded`)

### Önemli API Metotları:
1. `get_system_configurations` (Sistem ayarları ve sürüm kontrolü)
2. `get_languages` (Aktif sistem dilleri listesi)
3. `get_categories` (Kategoriler)
4. `get_questions` (Seviye ve kategoriye göre sorular)
5. `get_daily_quiz` (Günün soruları)
6. `get_daily_leaderboard` & `get_monthly_leaderboard` (Liderlik sıralaması)
7. `user_signup` / `get_user_by_id` (Kullanıcı profili senkronizasyonu)
8. `set_user_coin_score` (Skor ve jeton güncelleme)
