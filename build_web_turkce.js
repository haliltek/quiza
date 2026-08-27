const fs = require('fs');

const webTranslations = {
    "home": "Ana Sayfa",
    "quiz": "Testler",
    "categories": "Kategoriler",
    "leaderboard": "Liderlik Tablosu",
    "aboutUs": "Hakkımızda",
    "contactUs": "İletişim",
    "privacyPolicy": "Gizlilik Politikası",
    "termsAndConditions": "Hüküm ve Koşullar",
    "login": "Giriş Yap",
    "register": "Kayıt Ol",
    "logout": "Çıkış Yap",
    "profile": "Profilim",
    "settings": "Ayarlar",
    "playNow": "Hemen Oyna",
    "score": "Puan",
    "coins": "Jeton",
    "rank": "Sıra",
    "totalQuestions": "Toplam Soru",
    "correctAnswers": "Doğru Cevaplar",
    "incorrectAnswers": "Yanlış Cevaplar",
    "timeTaken": "Geçen Süre",
    "result": "Sonuç",
    "nextQuestion": "Sonraki Soru",
    "previousQuestion": "Önceki Soru",
    "submit": "Tamamla",
    "tryAgain": "Tekrar Dene",
    "viewAll": "Tümünü Gör",
    "search": "Ara...",
    "noDataFound": "Veri Bulunamadı",
    "loading": "Yükleniyor...",
    "language": "Dil Seçimi",
    "theme": "Tema",
    "dark": "Koyu",
    "light": "Açık",
    "system": "Sistem"
};

const originalWebData = JSON.parse(fs.readFileSync('d:/quiza/web_turkce.json', 'utf8'));

for (const key in originalWebData) {
    if (webTranslations[key]) {
        originalWebData[key] = webTranslations[key];
    } else {
        let val = originalWebData[key];
        val = val.replace(/Home/gi, "Ana Sayfa");
        val = val.replace(/Quiz/gi, "Test");
        val = val.replace(/Categories/gi, "Kategoriler");
        val = val.replace(/Category/gi, "Kategori");
        val = val.replace(/Leaderboard/gi, "Liderlik Tablosu");
        val = val.replace(/About Us/gi, "Hakkımızda");
        val = val.replace(/Contact Us/gi, "İletişim");
        val = val.replace(/Privacy Policy/gi, "Gizlilik Politikası");
        val = val.replace(/Terms and Conditions/gi, "Hüküm ve Koşullar");
        val = val.replace(/Login/gi, "Giriş Yap");
        val = val.replace(/Register/gi, "Kayıt Ol");
        val = val.replace(/Logout/gi, "Çıkış Yap");
        val = val.replace(/Profile/gi, "Profil");
        val = val.replace(/Settings/gi, "Ayarlar");
        val = val.replace(/Play Now/gi, "Hemen Oyna");
        val = val.replace(/Score/gi, "Puan");
        val = val.replace(/Coins/gi, "Jeton");
        val = val.replace(/Rank/gi, "Sıra");
        val = val.replace(/Total Questions/gi, "Toplam Soru");
        val = val.replace(/Correct Answers/gi, "Doğru Cevaplar");
        val = val.replace(/Incorrect Answers/gi, "Yanlış Cevaplar");
        val = val.replace(/Result/gi, "Sonuç");
        val = val.replace(/Next/gi, "Sonraki");
        val = val.replace(/Previous/gi, "Önceki");
        val = val.replace(/Submit/gi, "Gönder");
        val = val.replace(/Try Again/gi, "Tekrar Dene");
        val = val.replace(/View All/gi, "Tümünü Gör");
        val = val.replace(/Search/gi, "Ara");
        val = val.replace(/Loading/gi, "Yükleniyor");
        originalWebData[key] = val;
    }
}

fs.writeFileSync('d:/quiza/web_turkce.json', JSON.stringify(originalWebData, null, 4), 'utf8');
console.log('Web Turkish translation file generated!');
