const fs = require('fs');

// Everyday Turkish translation dictionary for System Languages (CodeIgniter Admin Panel)
const dict = {
    // General / Common
    "submit": "Gönder",
    "view_update_delete": "Görüntüle / Güncelle / Sil",
    "view_update": "Görüntüle / Güncelle",
    "filter_data": "Verileri Filtrele",
    "id": "ID",
    "operate": "İşlem",
    "leave_it_blank": "( Değiştirmek istemiyorsanız boş bırakın )",
    "close": "Kapat",
    "save_changes": "Değişiklikleri Kaydet",
    "image_type_supported": "Desteklenen görsel formatları (png, jpg ve jpeg)",
    "svg_image_type_supported": "Desteklenen görsel formatları (png, jpg, jpeg ve svg)",
    "language_id": "Dil ID",
    "language": "Dil",
    "select_language": "Dil Seçin",
    "please_wait": "Lütfen bekleyin...",
    "Invalid_Image_Type": "Geçersiz Görsel Tipi",
    "Modification_in_demo_version_is_not_allowed": "Demo sürümünde değişiklik yapılmasına izin verilmiyor.",
    "You_are_not_authorize_to_operate_on_the_module": "Bu modülde işlem yapma yetkiniz bulunmuyor",
    "Only_Audio_allow": "Sadece ses dosyalarına izin verilir!",
    "Invalid_Audio_Type": "Geçersiz Ses Tipi",
    "audio_question_created_successfully": "Sesli soru başarıyla oluşturuldu!",
    "audio_question_updated_successfully": "Sesli soru başarıyla güncellendi!",
    "Only_png_jpg_and_jpeg_or_webp_image_allow": "Sadece png, jpg, jpeg veya webp görsellerine izin verilir!",
    "badge_updated_successfully": "Rozet başarıyla güncellendi!",
    "category_created_successfully": "Kategori başarıyla oluşturuldu!",
    "category_updated_successfully": "Kategori başarıyla güncellendi!",
    "category_order_updated_successfully": "Kategori sıralaması başarıyla güncellendi!",
    "subcategory_order_updated_successfully": "Alt kategori sıralaması başarıyla güncellendi!",
    "data_created_successfully": "Veri başarıyla oluşturuldu!",
    "data_updated_successfully": "Veri başarıyla güncellendi!",
    "status_updated_successfully": "Durum başarıyla güncellendi!",
    "product_id_already_exists": "Bu Ürün ID zaten mevcut",
    "file_upload_failed": "Dosya yükleme başarısız",
    "csv_file_successfully_imported": "CSV dosyası başarıyla içe aktarıldı!",
    "please_upload_data_in_csv_file": "Lütfen verileri CSV dosyası olarak yükleyin!",
    "please_fill_all_the_data_in_csv_file": "Lütfen CSV dosyasındaki tüm verileri doldurun!",
    "question_created_successfully": "Soru başarıyla oluşturuldu!",
    "question_updated_successfully": "Soru başarıyla güncellendi!",
    "successfully_prize_distributed_for": "Ödüller başarıyla dağıtıldı:",
    "prize_can_not_distributed_for": "Ödüller dağıtılamadı:",
    "prize_already_distributed_for": "Ödüller zaten dağıtılmış:",
    "prize_distribution_is_currently_not_available_check_contest_end_date": "Ödül dağıtımı şu an kullanılamıyor. Yarışma bitiş tarihini kontrol edin!",
    "contest_created_successfully": "Yarışma başarıyla oluşturuldu!",
    "contest_updated_successfully": "Yarışma başarıyla güncellendi!",
    "not_enought_question_for_active_contest": "Aktif yarışma için yeterli soru yok!",
    "prize_created_successfully": "Ödül başarıyla oluşturuldu!",
    "prize_updated_successfully": "Ödül başarıyla güncellendi!",
    "user_created_successfully": "Kullanıcı başarıyla oluşturuldu!",
    "user_updated_successfully": "Kullanıcı başarıyla güncellendi!",
    "daily_quiz_created_successfully": "Günün testi başarıyla oluşturuldu!",
    "daily_quiz_updated_successfully": "Günün testi başarıyla güncellendi!",
    "data_deleted_successfully": "Veri başarıyla silindi!",
    "exam_module_created_successfully": "Sınav modülü başarıyla oluşturuldu!",
    "exam_module_updated_successfully": "Sınav modülü başarıyla güncellendi!",
    "exam_module_question_created_successfully": "Sınav soruları başarıyla oluşturuldu!",
    "exam_module_question_updated_successfully": "Sınav soruları başarıyla güncellendi!",
    "fun_n_learn_created_successfully": "Öğren & Yarış modülü başarıyla oluşturuldu!",
    "fun_n_learn_updated_successfully": "Öğren & Yarış modülü başarıyla güncellendi!",
    "fun_n_learn_question_created_successfully": "Öğren & Yarış soruları başarıyla oluşturuldu!",
    "fun_n_learn_question_updated_successfully": "Öğren & Yarış soruları başarıyla güncellendi!",
    "guess_the_word_created_successfully": "Kelime Tahmini başarıyla oluşturuldu!",
    "guess_the_word_updated_successfully": "Kelime Tahmini başarıyla güncellendi!",
    "guess_the_word_question_created_successfully": "Kelime Tahmini soruları başarıyla oluşturuldu!",
    "guess_the_word_question_updated_successfully": "Kelime Tahmini soruları başarıyla güncellendi!",
    "language_created_successfully": "Dil başarıyla oluşturuldu!",
    "language_updated_successfully": "Dil başarıyla güncellendi!",
    "maths_question_created_successfully": "Matematik soruları başarıyla oluşturuldu!",
    "maths_question_updated_successfully": "Matematik soruları başarıyla güncellendi!",
    "multi_match_created_successfully": "Karma Eşleştirme başarıyla oluşturuldu!",
    "multi_match_updated_successfully": "Karma Eşleştirme başarıyla güncellendi!",
    "multi_match_question_created_successfully": "Karma Eşleştirme soruları başarıyla oluşturuldu!",
    "multi_match_question_updated_successfully": "Karma Eşleştirme soruları başarıyla güncellendi!",
    "notification_created_successfully": "Bildirim başarıyla oluşturuldu!",
    "notification_updated_successfully": "Bildirim başarıyla güncellendi!",
    "slider_created_successfully": "Slayt görseli başarıyla oluşturuldu!",
    "slider_updated_successfully": "Slayt görseli başarıyla güncellendi!",
    "subcategory_created_successfully": "Alt kategori başarıyla oluşturuldu!",
    "subcategory_updated_successfully": "Alt kategori başarıyla güncellendi!",
    "user_coin_updated_successfully": "Kullanıcı jetonları başarıyla güncellendi!",
    "user_status_updated_successfully": "Kullanıcı durumu başarıyla güncellendi!",
    "already_register_user_or_email": "Bu e-posta veya kullanıcı adı zaten kayıtlı!",
    "user_profile_updated_successfully": "Kullanıcı profili başarıyla güncellendi!",
    "settings_updated_successfully": "Ayarlar başarıyla güncellendi!",
    "web_settings_updated_successfully": "Web ayarları başarıyla güncellendi!",
    "Invalid_credentials": "Geçersiz giriş bilgileri!",
    "login_successfully": "Başarıyla giriş yapıldı!",
    "Invalid_or_expired_token": "Geçersiz veya süresi dolmuş anahtar",
    "password_updated_successfully": "Şifre başarıyla güncellendi!",
    "admin_profile_updated_successfully": "Yönetici profili başarıyla güncellendi!",
    "email_not_registered": "E-posta adresi kayıtlı değil!",
    "password_reset_link_sent_to_your_email": "Şifre sıfırlama bağlantısı e-posta adresinize gönderildi!",
    "password_reset_link_sent": "Şifre sıfırlama bağlantısı gönderildi!",
    "all_fields_are_required": "Tüm alanların doldurulması zorunludur!",

    // Admin Navigation & Section Headers
    "dashboard": "Kontrol Paneli",
    "categories": "Kategoriler",
    "subcategories": "Alt Kategoriler",
    "questions": "Sorular",
    "daily_quiz": "Günün Testi",
    "contests": "Yarışmalar",
    "fun_n_learn": "Öğren & Yarış",
    "guess_the_word": "Kelime Tahmini",
    "audio_questions": "Sesli Sorular",
    "maths_questions": "Matematik Soruları",
    "exam_module": "Sınav Modülü",
    "users": "Kullanıcılar",
    "leaderboard": "Liderlik Tablosu",
    "notifications": "Bildirimler",
    "system_settings": "Sistem Ayarları",
    "languages": "Diller",
    "system_languages": "Sistem Dilleri",
    "app_languages": "Uygulama Dilleri",
    "web_languages": "Web Dilleri",
    "settings": "Ayarlar",
    "profile": "Profil",
    "logout": "Çıkış Yap",
    "manage": "Yönet",
    "create": "Oluştur",
    "edit": "Düzenle",
    "delete": "Sil",
    "action": "Eylem",
    "actions": "Eylemler",
    "status": "Durum",
    "active": "Aktif",
    "deactive": "Pasif",
    "disabled": "Devre Dışı",
    "enabled": "Etkin",
    "title": "Başlık",
    "name": "İsim",
    "description": "Açıklama",
    "image": "Görsel",
    "icon": "İkon",
    "date": "Tarih",
    "time": "Zaman",
    "type": "Tip",
    "option": "Seçenek",
    "options": "Seçenekler",
    "answer": "Cevap",
    "correct_answer": "Doğru Cevap",
    "note": "Not",
    "coins": "Jetonlar",
    "score": "Puan",
    "rank": "Sıra",
    "level": "Seviye",
    "order": "Sıralama",
    "search": "Ara",
    "reset": "Sıfırla",
    "export": "Dışa Aktar",
    "import": "İçe Aktar",
    "back": "Geri",
    "yes": "Evet",
    "no": "Hayır",
    "cancel": "İptal",
    "confirm": "Onayla",
    "delete_confirm": "Silmek istediğinizden emin misiniz?",
    "success": "Başarılı",
    "warning": "Uyarı",
    "error": "Hata",
    "info": "Bilgi"
};

// Function to convert English phrase to natural everyday Turkish
function autoTranslate(key, origVal) {
    if (dict[key]) return dict[key];
    
    let text = origVal;
    
    // Pattern replacements
    text = text.replace(/created successfully/gi, "başarıyla oluşturuldu");
    text = text.replace(/updated successfully/gi, "başarıyla güncellendi");
    text = text.replace(/deleted successfully/gi, "başarıyla silindi");
    text = text.replace(/imported successfully/gi, "başarıyla içe aktarıldı");
    text = text.replace(/Select Language/gi, "Dil Seçin");
    text = text.replace(/Select Category/gi, "Kategori Seçin");
    text = text.replace(/Select Subcategory/gi, "Alt Kategori Seçin");
    text = text.replace(/Question/gi, "Soru");
    text = text.replace(/Questions/gi, "Sorular");
    text = text.replace(/Category/gi, "Kategori");
    text = text.replace(/Categories/gi, "Kategoriler");
    text = text.replace(/Subcategory/gi, "Alt Kategori");
    text = text.replace(/Subcategories/gi, "Alt Kategoriler");
    text = text.replace(/Language/gi, "Dil");
    text = text.replace(/Languages/gi, "Diller");
    text = text.replace(/User/gi, "Kullanıcı");
    text = text.replace(/Users/gi, "Kullanıcılar");
    text = text.replace(/Contest/gi, "Yarışma");
    text = text.replace(/Contests/gi, "Yarışmalar");
    text = text.replace(/Notification/gi, "Bildirim");
    text = text.replace(/Notifications/gi, "Bildirimler");
    text = text.replace(/Option/gi, "Seçenek");
    text = text.replace(/Options/gi, "Seçenekler");
    text = text.replace(/Correct Answer/gi, "Doğru Cevap");
    text = text.replace(/Daily Quiz/gi, "Günün Testi");
    text = text.replace(/Fun N Learn/gi, "Öğren & Yarış");
    text = text.replace(/Guess The Word/gi, "Kelime Tahmini");
    text = text.replace(/Maths Quiz/gi, "Matematik Yarışması");
    text = text.replace(/Audio Question/gi, "Sesli Soru");
    text = text.replace(/Exam Module/gi, "Sınav Modülü");
    text = text.replace(/Leaderboard/gi, "Liderlik Tablosu");
    text = text.replace(/System Settings/gi, "Sistem Ayarları");
    text = text.replace(/Web Settings/gi, "Web Ayarları");
    text = text.replace(/Privacy Policy/gi, "Gizlilik Politikası");
    text = text.replace(/Terms & Conditions/gi, "Hüküm ve Koşullar");
    text = text.replace(/About Us/gi, "Hakkımızda");
    text = text.replace(/Contact Us/gi, "İletişim");
    text = text.replace(/Instructions/gi, "Yönergeler");
    text = text.replace(/Manage/gi, "Yönet");
    text = text.replace(/Create/gi, "Oluştur");
    text = text.replace(/Edit/gi, "Düzenle");
    text = text.replace(/Delete/gi, "Sil");
    text = text.replace(/Status/gi, "Durum");
    text = text.replace(/Active/gi, "Aktif");
    text = text.replace(/Deactive/gi, "Pasif");
    text = text.replace(/View/gi, "Görüntüle");
    text = text.replace(/Filter/gi, "Filtrele");
    text = text.replace(/Search/gi, "Ara");
    text = text.replace(/Reset/gi, "Sıfırla");
    text = text.replace(/Save/gi, "Kaydet");
    text = text.replace(/Submit/gi, "Gönder");
    text = text.replace(/Close/gi, "Kapat");

    return text;
}

const content = fs.readFileSync('d:/quiza/turkce_lang.php', 'utf8');
const lines = content.split('\n');
let modifiedCount = 0;

const newLines = lines.map(line => {
    const match = line.match(/\$lang\['([^']+)'\]\s*=\s*"([^"]*)";/);
    if (match) {
        const key = match[1];
        const origVal = match[2];
        const newVal = autoTranslate(key, origVal);
        modifiedCount++;
        return `$lang['${key}'] = "${newVal}";`;
    }
    return line;
});

fs.writeFileSync('d:/quiza/turkce_lang.php', newLines.join('\n'), 'utf8');
console.log(`Processed ${modifiedCount} system language keys for turkce_lang.php!`);
