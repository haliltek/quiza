# Elite Quiz v2.3.8 - Android Studio & Google Play Yayınlama Rehberi

Bu rehber, Elite Quiz mobil uygulamasını local bilgisayarınızdaki Android Studio ortamında çalıştırmanızı, Firebase entegrasyonunu tamamlamanızı ve Google Play Store'da yayınlamak için App Bundle (`.aab`) oluşturmanızı adım adım açıklar.

---

## 1. Firebase Projesi Kurulumu & Yapılandırma

1. **Firebase Console'a Gitme**:
   [Firebase Console](https://console.firebase.google.com/) adresine gidin ve yeni bir proje oluşturun (`Elite Quiz`).

2. **Android Uygulaması Ekleme**:
   - Paket adınızı belirtin (Örn: `com.yourcompany.elitequiz`).
   - Android Studio terminalinizden **SHA-1** ve **SHA-256** anahtarlarınızı alın:
     ```bash
     cd android
     ./gradlew :app:signingReport
     ```
   - Elde edilen SHA-1 ve SHA-256 değerlerini Firebase Android uygulamanıza ekleyin.

3. **`google-services.json` İndirme ve Ekleme**:
   - İndirdiğiniz `google-services.json` dosyasını Flutter projesinin `android/app/google-services.json` konumuna yerleştirin.

4. **Firestore & Authentication Etkinleştirme**:
   - Authentication bölümünden **Google**, **E-posta/Şifre** ve **Telefon** girişlerini aktif edin.
   - Firestore Database oluşturun ve okuma/yazma kurallarını (Rules) dökümantasyondaki gibi ayarlayın.

---

## 2. Android Studio'da Uygulamayı Çalıştırma (Debug Modu)

1. Projenizi Android Studio ile açın.
2. Terminal üzerinden paketleri indirin:
   ```bash
   flutter pub get
   ```
3. API Base URL adresinizi `lib/commons/constants.dart` veya ilgili konfigürasyon dosyasından sunucu adresiniz olarak ayarlayın:
   ```dart
   const String baseUrl = "http://142.93.104.78:8088/api/";
   ```
4. Bir Android Emulator veya USB Hata Ayıklama modundaki fiziksel cihazınızı bağlayıp çalıştırın:
   ```bash
   flutter run
   ```

---

## 3. Release Keystore Üretimi & `key.properties`

Google Play Store'a yüklemek için uygulamanın dijital olarak imzalanması gerekmektedir.

1. **Keystore Oluşturma (Terminal / Command Prompt)**:
   ```bash
   keytool -genkeypair -v -keystore elitequiz_release.jks -alias elitequiz -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **`android/key.properties` Dosyası Oluşturma**:
   `android/key.properties` adında bir dosya oluşturun ve içerisine bilgilerinizi yazın:
   ```properties
   storePassword=sizin_keystore_sifreniz
   keyPassword=sizin_key_sifreniz
   keyAlias=elitequiz
   storeFile=../elitequiz_release.jks
   ```

3. **Release App Bundle (`.aab`) Derleme**:
   ```bash
   flutter build appbundle --release
   ```
   Çıktı dosyası: `build/app/outputs/bundle/release/app-release.aab`

---

## 4. Google Play Console Yayın Adımları

1. [Google Play Console](https://play.google.com/apps/publish) hesabınıza giriş yapın.
2. **Yeni Uygulama Oluştur**: Uygulama adı, varsayılan dil (Türkçe), Ücretsiz/Ücretli durumunu seçin.
3. **Magaza Girişi (Main Store Listing)**:
   - Uygulama açıklaması, kısa açıklama.
   - Uygulama ikonu (512x512 PNG).
   - Öne çıkarılan grafik (1024x500 PNG).
   - En az 2 adet telefon ekran görüntüsü.
4. **İçerik Derecelendirmesi & Gizlilik Politikası**:
   - Gizlilik Politikası (Privacy Policy) URL'sini ekleyin.
   - Anket sorularını yanıtlayarak yaş derecelendirmesini tamamlayın.
5. **Üretim (Production) / Kapalı Test (Closed Testing)**:
   - Oluşturduğunuz `app-release.aab` dosyasını yükleyin.
   - İncelemeye Gönder (Submit for Review) butonuna tıklayın.
