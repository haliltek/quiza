# Quiza (Elite Quiz v2.3.9.1) — Ana Proje ve Geliştirme Portalı

Bu depo, **Quiza (Elite Quiz v2.3.9.1)** ekosisteminin tüm kaynak kodlarını, canlı sunucu altyapısını, mobil uygulama bileşenlerini ve geliştirici dökümantasyonunu barındırmaktadır.

---

## 🚀 Canlı Sunucu ve Yönetim Paneli Durumu

- **Yönetim Paneli Adresi:** [http://142.93.104.78:8088](http://142.93.104.78:8088)
- **RESTful API Endpoint:** `http://142.93.104.78:8088/api/`
- **Varsayılan Giriş Bilgileri:**
  - Kullanıcı Adı: `admin`
  - Şifre: `admin123`
- **Sunucu Altyapısı:** Docker Compose (Nginx Alpine + PHP 8.1 FPM + MySQL 8.0)
- **Sunucu İzolasyonu:** Sunucu üzerindeki diğer 4 bağımsız proje (`portfolio-2025`, `kizkiza`, `sharka-web`, `pokebook-web`) ile tamamen izole, bağımsız köprü ağında (`elitequiz_net`) çalışmaktadır.

---

## 📚 Kapsamlı Geliştirici Belgeleri

Projenin her aşaması için detaylı teknik kılavuzlar hazırlanmıştır:

1. 🏛️ **[Sistem Mimarisi (SYSTEM_ARCHITECTURE.md)](file:///d:/quiza/SYSTEM_ARCHITECTURE.md)**  
   Uçtan uca sistem topolojisi, veri akışları, güvenlik mekanizmaları ve katmanlar.

2. 🖥️ **[Sunucu Kurulum & Operasyon (SERVER_DEPLOYMENT.md)](file:///d:/quiza/SERVER_DEPLOYMENT.md)**  
   Docker container yönetimi, Nginx & PHP ayarları, günlük bakım, log takibi ve yedekleme prosedürleri.

3. 🎛️ **[Yönetim Paneli & API Kılavuzu (ADMIN_PANEL_GUIDE.md)](file:///d:/quiza/ADMIN_PANEL_GUIDE.md)**  
   Soru bankası, kategoriler, v2.3.9 Yapay Zeka (AI) ile soru üretimi, sistem ayarları ve API referansı.

4. 🗄️ **[Veritabanı Veri Sözlüğü (DATABASE_DICTIONARY.md)](file:///d:/quiza/DATABASE_DICTIONARY.md)**  
   56 MySQL tablosunun şema dökümü, sütun tipleri, indeksler ve ilişkisel bağlantılar.

5. 📱 **[Flutter Mobil & Mağaza Yayın Yol Haritası (FLUTTER_MOBILE_ROADMAP.md)](file:///d:/quiza/FLUTTER_MOBILE_ROADMAP.md)**  
   Flutter 3.38+ mimarisi, marka özelleştirme, Firebase/AdMob/IAP entegrasyonu ve Google Play / Apple App Store yayın kontrol listesi.

---

## 📂 Dizin ve Dosya Haritası

```
d:\quiza/
├── Elite Quiz - Admin Panel - v2.3.9.1/   # Orijinal panel kaynak zip ve güncelleme scriptleri
├── Elite Quiz - App - v2.3.9.1/           # Flutter 3.38+ kaynak kodu (Android & iOS)
├── elite_quiz_doc-main/                   # Resmi Docusaurus dokümantasyon kaynağı
├── elitequiz-2391/                        # v2.3.9.1 dağıtım paketleri ve changelog
├── SYSTEM_ARCHITECTURE.md                 # Sistem mimarisi ve bileşen şeması
├── SERVER_DEPLOYMENT.md                   # Uzak sunucu Docker ve Nginx kılavuzu
├── ADMIN_PANEL_GUIDE.md                   # Yönetim paneli ve API kılavuzu
├── DATABASE_DICTIONARY.md                 # MySQL 8.0 veri sözlüğü
├── FLUTTER_MOBILE_ROADMAP.md              # Mobil uygulama ve mağaza yayın rehberi
└── README.md                              # Ana proje portalı (Bu dosya)
```

---

## 🎯 Sonraki Geliştirme Aşamaları

1. **Aşama 1 (Tamamlandı):** Uzak sunucudaki eski quiz sisteminin temizlenmesi, v2.3.9.1 PHP/MySQL Docker kurulumunun tamamlanması ve admin panelinin canlıya alınması.
2. **Aşama 2 (Sıradaki):** Admin panelinde sistem dillerinin (Türkçe) yapılandırılması, genel ayarların tamamlanması ve Web arayüzünün bağlanması.
3. **Aşama 3:** Flutter mobil uygulamasının Quiza markasıyla giydirilmesi, Firebase ve AdMob hesaplarının bağlanması, Google Play Store ve Apple App Store için release derlemelerinin (AAB ve IPA) alınması.
