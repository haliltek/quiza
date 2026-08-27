# Elite Quiz v2.3.8 - Genel Mimarisi ve Ekosistem Dokümanı

## 1. Proje Özeti
**Elite Quiz v2.3.8**, çoklu platform desteğine sahip (Mobil Android & iOS, Web ve Yönetim Paneli) kapsamlı bir yarışma ve bilgi oyunu ekosistemidir.

### Mimarinin Ana Bileşenleri
```
┌─────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────────┐
│     Yönetim Paneli      │    │        Web App          │    │     Mobil Uygulama      │
│  (CodeIgniter 3 - PHP)  │    │       (Next.js)         │    │        (Flutter)        │
│                         │    │                         │    │                         │
│ • MySQL Veritabanı      │    │ • Kullanıcı Arayüzü     │    │ • Android & iOS         │
│   - Sorular & Kategoriler│    │ • Test Çözme Modülleri  │    │ • AdMob & Unity Ads     │
│   - Kullanıcı Verileri  │    │ • Liderlik Tablosu      │    │ • Uygulama İçi Satın   │
│   - Sistem Ayarları     │    │ • Sosyal Paylaşım       │    │   Alma (Jeton/Coin)     │
│                         │    │                         │    │ • Push Notifications    │
│ • REST API              │    │                         │    │                         │
└────────────┬────────────┘    └────────────┬────────────┘    └────────────┬────────────┘
             │                              │                              │
             └──────────────────────────────┼──────────────────────────────┘
                                            │
                                 ┌──────────┴──────────┐
                                 │      Firebase       │
                                 │                     │
                                 │ • Authentication    │
                                 │   - Google, Email   │
                                 │   - Telefon, Apple  │
                                 │ • Firestore         │
                                 │   - 1v1 Düello      │
                                 │   - Grup Düelloları │
                                 │   - Canlı Mesajlaşma│
                                 └─────────────────────┘
```

---

## 2. Modüller ve Özellikler

### A. Yönetim Paneli (Admin Panel - CodeIgniter 3 / PHP 8.1+)
- **Konum**: Zip içerisindeki `PHP CODE 2.3.8.zip` dosyası.
- **Görevler**:
  - Kategoriler, Alt Kategoriler, Soru Bankası yönetimi.
  - Çoklu dil (Language Mode) yönetimi.
  - Kullanıcılar, Skorlar, Jeton/Coin fiyatlandırması ve Para Çekme talepleri yönetimi.
  - Günlük Test (Daily Quiz), Yarışma (Contest), Doğru/Yanlış ve Sesli/Görselli Soru modları.
  - Firebase `serviceAccountKey.json` entegrasyonu (Push Bildirimleri ve Düello yönetimi için).

### B. Mobil Uygulama (Flutter)
- **Desteklenen Platformlar**: Android & iOS (Ana Hedef: Android - Google Play).
- **Entegrasyonlar**:
  - **Firebase Auth**: Google ile Giriş, E-posta, Telefon (SMS) ve Misafir Girişi.
  - **Firebase Firestore**: Gerçek zamanlı 1v1 Düello (Synchronized) ve Grup Düelloları (Asynchronous - 4 kişiye kadar).
  - **Google AdMob & Unity Ads**: Banner, Geçiş (Interstitial) ve Ödüllü (Rewarded) Reklamlar.
  - **In-App Purchase (IAP)**: Jeton satın alma ve Reklamları Kaldırma.

### C. Web Uygulaması (Next.js)
- **Konum**: `Elite Quiz Web v-2.3.8` klasörü.
- **Görevler**: Kullanıcıların web tarayıcısı üzerinden test çözmesini, liderlik tablosunu incelemesini ve skor kazanmasını sağlar.

---

## 3. Sistem Gereksinimleri
- **PHP**: >= 8.1 (Gerekli eklentiler: `mysqli`, `pdo_mysql`, `curl`, `gd`, `zip`, `mbstring`, `json`).
- **Veritabanı**: MySQL 5.7+ veya MariaDB 10.3+.
- **Sunucu**: Nginx / Apache (`.htaccess` ve `mod_rewrite` etkin olmalı).
- **Mobil**: Flutter SDK 3.x+, Android Studio, JDK 17+.
