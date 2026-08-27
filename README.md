# Quiza (Elite Quiz v2.3.8) - Kapsamlı Proje & Kurulum Rehberi

Bu depo, **Quiza (Elite Quiz v2.3.8)** ekosisteminin tüm bileşenlerini (Yönetim Paneli, Web Uygulaması, Mobil Uygulama ve Akıllı Ajan Yapılandırmalarını) içermektedir.

---

## 🚀 Proje Mimarisi

Quiza ekosistemi 3 ana katmandan oluşur:

1. **Yönetim Paneli (Admin Panel & API):**
   - **Teknoloji:** PHP 8.1 (CodeIgniter 3), MySQL 8.0, Nginx
   - **Canlı Sunucu:** `https://142.93.104.78:8088` (Docker üzerinde aktif)
   - **Görevler:** Soru bankası, kategoriler, yarışmalar, jeton işlemleri, kullanıcılar ve bildirim yönetimi.

2. **Web Uygulaması (Next.js):**
   - **Teknoloji:** Next.js 14, React 18, Tailwind CSS, Redux Toolkit
   - **Konum:** `Elite Quiz Web v-2.3.8/Elite Quiz Web v-2.3.8`
   - **Görevler:** Web tarayıcısı üzerinden test çözme, liderlik tablosu inceleme.

3. **Mobil Uygulama (Flutter):**
   - **Teknoloji:** Flutter 3.x, Dart, Firebase Auth & Firestore, AdMob / Unity Ads
   - **Görevler:** Android ve iOS cihazlarda 1v1 düellolar, grup oyunları, sesli testler.

---

## 🛠️ MacBook (macOS) Üzerinde Geliştirme Ortamı Kurulumu

MacBook bilgisayarınızda projeyi çekip geliştirmeye devam etmek için aşağıdaki adımları uygulayın:

### 1. Depoyu Klonlama ve Hazırlık
```bash
git clone git@github.com:haliltek/quiza.git
cd quiza
```

### 2. Web Uygulamasını Çalıştırma (Next.js)
```bash
cd "Elite Quiz Web v-2.3.8/Elite Quiz Web v-2.3.8"

# Bağımlılıkları yükleyin
npm install

# Geliştirici sunucusunu başlatın
npm run dev
```
Uygulamaya **`http://localhost:3000`** adresinden erişebilirsiniz. `.env` dosyası canlı API adresine (`https://142.93.104.78:8088`) ayarlanmıştır.

### 3. Mobil Uygulamayı Çalıştırma (Flutter - macOS)
MacBook üzerinde iOS ve Android emülatörlerini çalıştırmak için:

1. **Gerekli Araçlar:** Flutter SDK, Android Studio, Xcode, CocoaPods
   ```bash
   brew install cocoapods
   flutter doctor
   ```
2. **API Yapılandırması:**
   `lib/commons/constants.dart` dosyasındaki API adresinin doğruluğunu kontrol edin:
   ```dart
   const String baseUrl = "https://142.93.104.78:8088/api/";
   ```
3. **Uygulamayı Çalıştırma:**
   ```bash
   flutter pub get
   
   # Android emülatör veya cihaz için
   flutter run -d android
   
   # iOS simülatör için
   cd ios && pod install && cd ..
   flutter run -d iphone
   ```

---

## 🌍 Türkçe Dil Paketi ve Çeviriler

Tüm uygulama katmanları %100 Türkçe (günlük kullanım dili) olarak yapılandırılmıştır:

- **Mobil Uygulama Çevirileri:** `upload/languages/app/turkce.json` (586 etiket)
- **Sistem Yönetim Paneli Çevirileri:** `application/language/turkce/turkce_lang.php` (949 etiket)
- **Web Uygulaması Çevirileri:** `upload/languages/web/turkce.json` (487 etiket)

---

## 📦 Sunucu (Docker) Kurulum Bilgileri

Canlı sunucudaki (`142.93.104.78`) Docker yapılandırması:

- `docker-compose.yml` ile başlatılan servisler:
  - `elitequiz_db` (MySQL 8.0)
  - `elitequiz_api` (PHP 8.1 FPM)
  - `elitequiz_webserver` (Nginx - Port 8088 / SSL Aktif)

Sunucuda güncelleme yapmak için:
```bash
ssh root@142.93.104.78
cd /opt/elitequiz
docker-compose restart
```

---

## 🤖 AG Kit / Akıllı Ajan Yapılandırmaları (`.agents`)

Proje kök dizininde yer alan `.agents` klasörü, Antigravity ve Gemini CLI ortamlarında kullanılan tüm kuralları, hafıza dizinini ve ajan yeteneklerini barındırır:
- `.agents/agent/`: Uzmanlık ajanları
- `.agents/rules/`: Proje kuralları ve yönlendirme protokolleri
- `.agents/skills/`: Sistem yetenekleri (i18n, clean-code, vs.)
- `.agents/memory/`: Kalıcı hafıza ve proje kararları

---

## 📝 Lisans ve Telif

Tüm hakları saklıdır. Bu proje özel kullanım ve Quiza ekosistemi geliştirmeleri için barındırılmaktadır.
