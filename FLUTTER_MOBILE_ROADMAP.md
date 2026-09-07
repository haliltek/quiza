# Quiza (Elite Quiz v2.3.9.1) — Flutter Mobil Uygulama & Mağaza Yayın Yol Haritası

Bu kılavuz, **Quiza (Elite Quiz v2.3.9.1)** mobil uygulamasının (`Elite Quiz - App - v2.3.9.1`) mimarisini, özelleştirme adımlarını, Firebase ve reklam entegrasyonlarını ve Google Play Store ile Apple App Store mağaza yayın süreçlerini adım adım açıklamaktadır.

---

## 1. Mobil Proje Mimarisi

- **Konum:** `d:\quiza\Elite Quiz - App - v2.3.9.1`
- **Flutter Sürüm Uyumluluğu:** Flutter 3.38.1+ / Dart 3.10+
- **Durum Yönetimi (State Management):** BLoC (`flutter_bloc: ^9.1.1`)
- **Lokal Depolama (Caching):** Hive (`hive_flutter: ^1.1.0`)
- **Ağ İletişimi:** `http: ^1.6.0`

### Dizin Yapısı (`lib/`):
```
lib/
├── commons/          # Ortak yardımcılar, sabitler (constants.dart) ve temalar
├── features/         # BLoC ve UI modülleri
│   ├── auth/         # Giriş, kayıt, SMS OTP ve sosyal login
│   ├── battle/       # 1v1 ve Grup Savaşları gerçek zamanlı oyun ekranları
│   ├── quiz/         # Soru çözme motoru, süre sayacı, can simitleri (50-50, Süre, vb.)
│   ├── profile/      # Profil, rozetler, istatistikler ve cüzdan
│   ├── leaderboard/  # Günlük ve aylık sıralama tabloları
│   └── ads/          # Reklam yöneticisi (AdMob, Unity, IronSource)
└── main.dart         # Başlangıç noktası ve servis başlatıcılar
```

---

## 2. API ve Sunucu Bağlantısı

Mobil uygulamanın canlı yönetim panelinize bağlanması için:
Dosya: `lib/commons/constants.dart` (veya `lib/constants.dart`):
```dart
// Canlı Yönetim Paneli API Adresi
const String baseUrl = "http://142.93.104.78:8088/api/";

// Varsayılan dil ve uygulama sabitleri
const String defaultLanguage = "tr";
```

---

## 3. Markalama ve Özelleştirme Adımları (Rebranding)

### A. Uygulama Adı & Paket İsmi (Package Name / Bundle ID)
- **Yeni Paket İsmi Önerisi:** `com.quiza.app`
- **Android:**
  - `android/app/build.gradle`: `applicationId "com.quiza.app"`
  - `android/app/src/main/AndroidManifest.xml`: paket ve intent tanımları.
- **iOS:**
  - `ios/Runner.xcodeproj/project.pbxproj`: `PRODUCT_BUNDLE_IDENTIFIER = com.quiza.app;`
  - Xcode üzerinden `Bundle Identifier` güncellemesi.

### B. Logo ve Uygulama İkonları
- `assets/images/` altındaki logo dosyalarının Quiza logosuyla değiştirilmesi.
- `flutter_launcher_icons.yaml` dosyasının çalıştırılması:
  ```bash
  flutter pub run flutter_launcher_icons
  ```

### C. Splash Screen (Açılış Ekranı)
- `android/app/src/main/res/drawable/` ve iOS LaunchScreen görsellerinin güncellenmesi.

---

## 4. Firebase Kurulumu

Canlı savaşlar (Battle Mode), bildirimler ve giriş için Firebase zorunludur:
1. **Firebase Console Projesi:** [console.firebase.google.com](https://console.firebase.google.com) üzerinde `Quiza` projesi açılır.
2. **Android Entegrasyonu:**
   - Paket adı (`com.quiza.app`) ile Android uygulaması eklenir.
   - İndirilen `google-services.json` dosyası `android/app/` dizinine yerleştirilir.
   - SHA-1 ve SHA-256 parmak izleri eklenir (Google Sign-In ve Phone Auth için şarttır).
3. **iOS Entegrasyonu:**
   - Bundle ID (`com.quiza.app`) ile iOS uygulaması eklenir.
   - İndirilen `GoogleService-Info.plist` dosyası `ios/Runner/` dizinine eklenir.
4. **Cloud Firestore:**
   - Firestore veritabanı oluşturulur.
   - `elite_quiz_doc-main/docs/common_firebase_config.md` içindeki güvenlik kuralları ve indeksler Firestore'a yapıştırılır.
5. **Firebase Authentication:**
   - E-posta/Şifre, Telefon (SMS), Google ve Apple giriş yöntemleri aktif edilir.
6. **Yönetim Paneline Hizmet Hesabı Yükleme:**
   - Firebase Console -> Proje Ayarları -> Hizmet Hesapları (Service Accounts) -> `Yeni Özel Anahtar Oluştur` seçilerek `serviceAccountKey.json` indirilir.
   - Yönetim paneli **Upload Services JSON** bölümünden yüklenir (Push bildirimleri için).

---

## 5. Gelir Modelleri: Reklam & Uygulama İçi Satın Alma (Monetization)

### Google AdMob Entegrasyonu:
1. `AndroidManifest.xml` içine AdMob App ID eklenir:
   ```xml
   <meta-data
       android:name="com.google.android.gms.ads.APPLICATION_ID"
       android:value="ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX"/>
   ```
2. `Info.plist` içine `GADApplicationIdentifier` ve SKAdNetwork kimlikleri eklenir.
3. Reklam Birim ID'leri (Banner, Geçiş, Ödüllü) yönetim panelinden (`System Configurations -> Ads`) girilir. Kod tarafında tekrar derleme gerektirmez.

### Uygulama İçi Satın Alma (In-App Purchases - IAP):
- Google Play Console ve App Store Connect'te jeton paketleri (örn: `coins_100`, `coins_500`) tanımlanır.
- Yönetim paneli **Coin Store** menüsüne ürün kimlikleri (Product ID) eklenir.

---

## 6. Google Play Store Yayın Kontrol Listesi

- [ ] **Android 15 & 16KB Sayfa Boyutu (16KB Page Size) Uyumluluğu:** v2.3.9 sürümüyle tam uyumlu hale getirilmiştir.
- [ ] **Sürüm Kodu ve Adı:** `pubspec.yaml` -> `version: 1.0.0+1`
- [ ] **İmzalama Anahtarı (Upload Keystore):**
  ```bash
  keytool -genkey -v -keystore upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
  ```
  `android/key.properties` dosyası oluşturulup yapılandırılır.
- [ ] **Android App Bundle (AAB) Üretimi:**
  ```bash
  flutter build appbundle --release
  ```
  Çıktı: `build/app/outputs/bundle/release/app-release.aab`
- [ ] **Play Console Gönderimi:** Hedef kitle (Trivia / Bilgi Yarışması), Gizlilik Politikası URL'si, Veri Güvenliği formu ve ekran görüntüleri tamamlanır.

---

## 7. Apple App Store Yayın Kontrol Listesi

- [ ] **Apple Developer Program:** Aktif geliştirici hesabı.
- [ ] **Sign in with Apple:** iOS üzerinde sosyal giriş varsa Apple ile Giriş zorunludur (kodda hazır entegredir).
- [ ] **App Tracking Transparency (ATT):** Reklam takibi izni için `Info.plist` metinleri.
- [ ] **IPA Üretimi & TestFlight:**
  ```bash
  flutter build ipa --release
  ```
- [ ] **Transporter:** Üretilen IPA Transporter uygulaması veya Xcode ile App Store Connect'e yüklenir.
- [ ] **İnceleme İçin Demo Hesap:** Apple inceleme ekibi için test kullanıcı adı/şifresi tanımlanır.
