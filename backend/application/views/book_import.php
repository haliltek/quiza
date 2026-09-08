<!DOCTYPE html>
<html lang="tr">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no" name="viewport">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>PDF & Kitap Soru İçe Aktarıcı | <?php echo (is_settings('app_name')) ? is_settings('app_name') : "Quiza" ?></title>
    <?php base_url() . include 'include.php'; ?>
    <style>
        .source-card {
            border-top: 4px solid #6777ef;
            box-shadow: 0 4px 12px rgba(0,0,0,.06);
            border-radius: 8px;
        }
        .preview-box {
            max-height: 600px;
            overflow-y: auto;
        }
        .q-card {
            border-left: 4px solid #3abaf4;
            margin-bottom: 15px;
            background: #fdfdff;
            border-radius: 6px;
        }
        .solution-box {
            background-color: #f4f6f9;
            border-radius: 6px;
            padding: 12px 16px;
            font-size: 0.92rem;
            color: #2c3246;
            border-left: 3px solid #28a745;
            line-height: 1.6;
        }
        .method-badge {
            font-size: 0.75rem;
            padding: 4px 8px;
            border-radius: 4px;
            text-transform: uppercase;
            font-weight: 700;
        }
        .tab-btn.active {
            background-color: #6777ef !important;
            color: #fff !important;
        }
    </style>
</head>

<body>
    <div id="app">
        <div class="main-wrapper">
            <?php base_url() . include 'header.php'; ?>

            <!-- Main Content -->
            <div class="main-content">
                <section class="section">
                    <div class="section-header">
                        <h1><em class="fas fa-file-pdf mr-2"></em> PDF & Kitap Soru İçe Aktarıcı</h1>
                        <div class="section-header-breadcrumb">
                            <div class="breadcrumb-item active"><a href="<?= base_url(); ?>dashboard">Panel</a></div>
                            <div class="breadcrumb-item">PDF & Kitap İçe Aktar</div>
                        </div>
                    </div>

                    <div class="section-body">
                        <!-- Success Banner for Already Imported Books -->
                        <div class="alert alert-success alert-has-icon shadow-sm mb-4">
                            <div class="alert-icon"><em class="fas fa-check-circle"></em></div>
                            <div class="alert-body">
                                <div class="alert-title font-weight-bold">HMGS Soru Bankaları Sisteme Aktarıldı!</div>
                                <strong>HMGS İdare Hukuku (238 Soru)</strong> ve <strong>HMGS Anayasa Hukuku (193 Soru)</strong> olmak üzere toplam <strong>431 adet soru</strong> ve detaylı kanuni çözümleri başarıyla veritabanına eklenmiştir. Bu soruları <em>Kategori 11 (Anayasa & İdare Hukuku)</em> altında görüntüleyebilir, testlerde ve düellolarda hemen kullanabilirsiniz.
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-12">
                                <div class="card source-card">
                                    <div class="card-header d-flex justify-content-between align-items-center">
                                        <h4><em class="fas fa-magic mr-2 text-primary"></em> Akıllı Kitap & PDF Analiz Motoru</h4>
                                        <span class="badge badge-success"><em class="fas fa-shield-alt mr-1"></em> PDF, Scribd & HTML Destekli</span>
                                    </div>
                                    <div class="card-body">
                                        <p class="text-muted mb-4">
                                            İnternetteki veya bilgisayarınızdaki soru bankalarını, deneme sınavlarını ya da Scribd kitaplarını sisteme otomatik olarak aktarın. Sistem soruları, şıkları (A-E), doğru cevapları ve detaylı çözümleri tek tek tespit eder.
                                        </p>

                                        <form id="importForm" enctype="multipart/form-data">
                                            <input type="hidden" name="<?= $this->security->get_csrf_token_name(); ?>" value="<?= $this->security->get_csrf_hash(); ?>">

                                            <!-- Method 1 & 2 Inputs -->
                                            <div class="row">
                                                <div class="form-group col-md-6">
                                                    <label class="font-weight-bold d-flex justify-content-between">
                                                        <span><em class="fas fa-file-upload text-success mr-1"></em> 1. Yöntem: Doğrudan PDF Dosyası Yükle</span>
                                                        <span class="badge badge-success method-badge">Önerilen & En Hızlı</span>
                                                    </label>
                                                    <input type="file" name="pdf_file" id="pdf_file" class="form-control" accept=".pdf">
                                                    <small class="form-text text-muted">Bilgisayarınızdaki PDF soru bankasını seçin. Tüm soru ve çözümler anında taranır.</small>
                                                </div>

                                                <div class="form-group col-md-6">
                                                    <label class="font-weight-bold d-flex justify-content-between">
                                                        <span><em class="fas fa-link text-primary mr-1"></em> 2. Yöntem: Kitap / PDF Web Linki</span>
                                                        <span class="badge badge-info method-badge">Web Linki</span>
                                                    </label>
                                                    <div class="input-group">
                                                        <div class="input-group-prepend">
                                                            <div class="input-group-text"><em class="fas fa-globe"></em></div>
                                                        </div>
                                                        <input type="url" name="url" id="doc_url" class="form-control" placeholder="https://.../sorular.pdf veya https://www.scribd.com/document/...">
                                                    </div>
                                                    <small class="form-text text-muted">Doğrudan PDF web adresi veya Scribd belge linki.</small>
                                                </div>
                                            </div>

                                            <!-- Method 3: Collapsible Scribd HTML Source Paste -->
                                            <div class="form-group">
                                                <div class="d-flex justify-content-between align-items-center mb-1">
                                                    <a class="btn btn-outline-secondary btn-sm" data-toggle="collapse" href="#htmlSourceCollapse" role="button" aria-expanded="false" aria-controls="htmlSourceCollapse">
                                                        <em class="fas fa-code mr-1"></em> 3. Yöntem: Scribd Sayfa Kaynağı (HTML) Yapıştır (Alternatif)
                                                    </a>
                                                    <small class="text-muted">Scribd bot koruması linki engellediğinde kullanılır.</small>
                                                </div>
                                                <div class="collapse mt-2" id="htmlSourceCollapse">
                                                    <div class="card card-body bg-light border p-3">
                                                        <label class="font-weight-bold text-dark mb-1">Scribd Sayfa Kaynağı (Ctrl+U):</label>
                                                        <textarea name="html_source" id="html_source" rows="4" class="form-control" placeholder="Scribd dokümanını tarayıcınızda açıp klavyeden Ctrl+U ile sayfa kaynağını kopyalayın ve buraya yapıştırın..."></textarea>
                                                        <small class="form-text text-muted mt-1">
                                                            <em class="fas fa-info-circle text-primary"></em> Tarayıcınız Scribd bot korumasına takılmadığı için kaynak kodunu buraya yapıştırdığınızda tüm sayfalar Cloud CDN üzerinden en yüksek hızda ve eksiksiz indirilir.
                                                        </small>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Category, Badge, Exam selection -->
                                            <div class="row">
                                                <div class="form-group col-md-4">
                                                    <label class="font-weight-bold">Hedef Kategori:</label>
                                                    <select name="category_id" id="category_id" class="form-control select2">
                                                        <option value="0" selected>⚡ Otomatik Branş Dağıtımı (Türkçe, Matematik, Tarih, Coğrafya, Vatandaşlık, Güncel)</option>
                                                        <?php foreach ($categories as $cat) { ?>
                                                            <option value="<?= $cat->id; ?>">
                                                                <?= $cat->id . ' - ' . $cat->category_name; ?>
                                                            </option>
                                                        <?php } ?>
                                                    </select>
                                                </div>

                                                <div class="form-group col-md-4">
                                                    <label class="font-weight-bold">Soru Rozeti / Etiketi (Opsiyonel):</label>
                                                    <input type="text" name="badge" id="badge" class="form-control" placeholder="Örn: HMGS İdare Hukuku, 2024 KPSS vb.">
                                                    <small class="form-text text-muted">Sorunun başında görünür: <code>[HMGS İdare Hukuku]</code></small>
                                                </div>

                                                <div class="form-group col-md-4">
                                                    <label class="font-weight-bold">Hedef Deneme Sınavı (Opsiyonel):</label>
                                                    <select name="exam_id" id="exam_id" class="form-control">
                                                        <option value="0">-- Genel Soru Bankasına Ekle (Sınava Bağlama) --</option>
                                                        <?php foreach ($exams as $ex) { ?>
                                                            <option value="<?= $ex->id; ?>">
                                                                <?= $ex->title; ?>
                                                            </option>
                                                        <?php } ?>
                                                    </select>
                                                    <small class="form-text text-muted">Seçilirse sorular bu deneme sınavına da bağlanır.</small>
                                                </div>
                                            </div>

                                            <div class="form-group mt-2">
                                                <button type="button" id="btnPreview" class="btn btn-primary btn-lg shadow-sm">
                                                    <em class="fas fa-search mr-2"></em> Kitabı / PDF'i Analiz Et ve Önizle
                                                </button>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Preview Card -->
                        <div class="row" id="previewContainer" style="display: none;">
                            <div class="col-12">
                                <div class="card border-success">
                                    <div class="card-header bg-light d-flex justify-content-between align-items-center">
                                        <h4 class="text-success"><em class="fas fa-list-check mr-2"></em> Analiz Sonucu: <span id="docTitle" class="text-dark"></span></h4>
                                        <div>
                                            <span class="badge badge-primary mr-2" id="totalCountBadge">0 Soru Tespit Edildi</span>
                                            <button type="button" id="btnConfirmSave" class="btn btn-success btn-lg shadow">
                                                <em class="fas fa-cloud-upload-alt mr-2"></em> Tüm Soruları ve Çözümleri Veritabanına Aktar
                                            </button>
                                        </div>
                                    </div>
                                    <div class="card-body">
                                        <div class="alert alert-info mb-3">
                                            <em class="fas fa-check-double mr-1"></em> Kitap içeriği başarıyla çözümlendi! Aşağıda tespit edilen ilk sorular, şıkları, doğru cevapları ve detaylı kanuni çözümleri önizlenmektedir. <strong>"Tüm Soruları ve Çözümleri Veritabanına Aktar"</strong> butonuna basarak soruları canlı sisteme aktarabilirsiniz.
                                        </div>

                                        <div class="preview-box" id="questionsPreviewList">
                                            <!-- Dynamically injected cards -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>
            </div>

            <?php base_url() . include 'footer.php'; ?>
        </div>
    </div>

    <script>
        $(document).ready(function () {
            $('#btnPreview').on('click', function (e) {
                e.preventDefault();

                var url = $('#doc_url').val().trim();
                var file = $('#pdf_file')[0].files[0];
                var htmlSource = $('#html_source').val().trim();

                if (!url && !file && !htmlSource) {
                    Swal.fire({
                        icon: "warning",
                        title: "Eksik Bilgi",
                        text: "Lütfen bir PDF dosyası seçin, link girin veya Scribd sayfa kaynağını yapıştırın."
                    });
                    return;
                }

                var formElement = document.getElementById('importForm');
                var formData = new FormData(formElement);
                var btn = $('#btnPreview');
                var originalHtml = btn.html();

                btn.prop('disabled', true).html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span> Belge İndiriliyor ve Analiz Ediliyor (Biraz zaman alabilir)...');
                $('#previewContainer').slideUp();

                $.ajax({
                    url: '<?= base_url("book-import/preview"); ?>',
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    dataType: 'json',
                    success: function (res) {
                        btn.prop('disabled', false).html(originalHtml);

                        // If Scribd Bot Challenge is triggered
                        if (res.is_bot_challenge) {
                            var docId = res.doc_id || '';
                            var embedUrl = res.embed_url || ('https://www.scribd.com/embeds/' + docId + '/content');

                            Swal.fire({
                                icon: "warning",
                                title: "Scribd Bot Güvenlik Kalkanı",
                                html: '<div class="text-left" style="font-size:0.95rem; line-height:1.6;">' +
                                      '<p>Scribd, sunucu üzerinden doğrudan web bağlantılarını güvenlik duvarı (Bot Koruması) ile sınırlandırmaktadır.</p>' +
                                      '<p class="font-weight-bold mb-2">Bu kitabı içeri aktarmak için 2 kolay yol mevcuttur:</p>' +
                                      '<div class="p-2 mb-2 bg-light border rounded">' +
                                      '<strong>1. Yöntem (En Hızlısı - PDF Yükleme):</strong><br>' +
                                      'Kitabı PDF olarak indirip soldaki <em>"Doğrudan PDF Dosyası Yükle"</em> kısmından seçebilirsiniz.' +
                                      '</div>' +
                                      '<div class="p-2 bg-light border rounded">' +
                                      '<strong>2. Yöntem (Sayfa Kaynağını Yapıştırma):</strong><br>' +
                                      '<a href="' + embedUrl + '" target="_blank" class="btn btn-sm btn-info my-1"><em class="fas fa-external-link-alt mr-1"></em> Scribd Belgesini Yeni Sekmede Aç</a><br>' +
                                      'Açılan sayfada <code>Ctrl+U</code> tuşlarına basarak tüm kaynak kodunu kopyalayın ve <em>"3. Yöntem: Scribd HTML Kaynağı"</em> kutusuna yapıştırın.' +
                                      '</div>' +
                                      '</div>',
                                showCancelButton: true,
                                confirmButtonText: '<em class="fas fa-code mr-1"></em> HTML Yapıştırma Kutusunu Aç',
                                cancelButtonText: '<em class="fas fa-file-pdf mr-1"></em> PDF Olarak Yükleyeceğim',
                                confirmButtonColor: '#6777ef',
                                cancelButtonColor: '#28a745'
                            }).then(function (result) {
                                if (result.isConfirmed) {
                                    $('#htmlSourceCollapse').collapse('show');
                                    $('#html_source').focus();
                                    $('html, body').animate({
                                        scrollTop: $("#htmlSourceCollapse").offset().top - 40
                                    }, 400);
                                } else {
                                    $('#pdf_file').click();
                                }
                            });
                            return;
                        }

                        if (res.is_scanned) {
                            Swal.fire({
                                icon: "info",
                                title: "Taranmış Görsel (Fotokopi) PDF",
                                html: '<div class="text-left" style="font-size:0.95rem; line-height:1.6;">' +
                                      '<p>Yüklediğiniz dosya matbaa veya fotokopi taraması (resim) olduğu için dosya içerisinde <strong>seçilebilir dijital metin katmanı bulunmamaktadır</strong>.</p>' +
                                      '<p class="font-weight-bold mb-1">Soruların eksiksiz ve hatasız aktarılabilmesi için:</p>' +
                                      '<ul class="pl-3">' +
                                      '<li>Metinleri fare ile seçilip kopyalanabilen <strong>orijinal dijital PDF soru bankalarını</strong> yükleyebilir,</li>' +
                                      '<li>Veya dokümanın <strong>Scribd linkini</strong> kullanarak tüm soruları ve detaylı çözümleri otomatik olarak çekebilirsiniz.</li>' +
                                      '</ul>' +
                                      '</div>',
                                confirmButtonText: "Anladım",
                                confirmButtonColor: "#6777ef"
                            });
                            return;
                        }

                        if (res.error) {
                            Swal.fire({
                                icon: "error",
                                title: "Analiz Edilemedi",
                                text: res.message
                            });
                            return;
                        }

                        $('#docTitle').text(res.title);
                        $('#totalCountBadge').text(res.total + ' Soru & Çözüm Tespit Edildi');

                        var listHtml = '';
                        $.each(res.preview, function (idx, q) {
                            listHtml += '<div class="card q-card p-3 shadow-sm">';
                            listHtml += '<div class="d-flex justify-content-between align-items-center mb-2">';
                            listHtml += '<div>';
                            listHtml += '<h6 class="text-primary font-weight-bold d-inline mr-2">Soru ' + (idx + 1) + '</h6>';
                            if (q.subject) {
                                listHtml += '<span class="badge badge-info mr-1">' + q.subject + '</span>';
                            }
                            if (q.test) {
                                listHtml += '<span class="badge badge-secondary">' + (q.test === 'GY' ? 'Genel Yetenek' : 'Genel Kültür') + '</span>';
                            }
                            listHtml += '</div>';
                            listHtml += '<span class="badge badge-success font-weight-bold">Doğru Cevap: ' + q.answer.toUpperCase() + '</span>';
                            listHtml += '</div>';

                            listHtml += '<p class="font-weight-bold mb-2">' + $('<div>').text(q.question).html() + '</p>';

                            listHtml += '<div class="row pl-3 mb-2">';
                            listHtml += '<div class="col-md-6 mb-1"><strong>A)</strong> ' + $('<div>').text(q.optiona).html() + '</div>';
                            listHtml += '<div class="col-md-6 mb-1"><strong>B)</strong> ' + $('<div>').text(q.optionb).html() + '</div>';
                            listHtml += '<div class="col-md-6 mb-1"><strong>C)</strong> ' + $('<div>').text(q.optionc).html() + '</div>';
                            listHtml += '<div class="col-md-6 mb-1"><strong>D)</strong> ' + $('<div>').text(q.optiond).html() + '</div>';
                            listHtml += '<div class="col-md-6 mb-1"><strong>E)</strong> ' + $('<div>').text(q.optione).html() + '</div>';
                            listHtml += '</div>';

                            if (q.solution && q.solution.trim() !== '') {
                                listHtml += '<div class="solution-box mt-2">';
                                listHtml += '<strong><em class="fas fa-balance-scale text-success mr-1"></em> Detaylı Çözüm & Kanuni Açıklama:</strong><br>';
                                listHtml += $('<div>').text(q.solution).html();
                                listHtml += '</div>';
                            }
                            listHtml += '</div>';
                        });

                        $('#questionsPreviewList').html(listHtml);
                        $('#previewContainer').slideDown();
                        $('html, body').animate({
                            scrollTop: $("#previewContainer").offset().top - 20
                        }, 500);
                    },
                    error: function (xhr, status, err) {
                        btn.prop('disabled', false).html(originalHtml);
                        var errMsg = "Sunucu isteği işlerken bir hata oluştu (" + err + ").";
                        if (xhr.status === 403) {
                            errMsg = "Oturumunuz zaman aşımına uğramış veya CSRF doğrulaması yenilenmiş olabilir. Lütfen sayfayı yenileyip tekrar deneyin.";
                        }
                        Swal.fire({
                            icon: "error",
                            title: "Bağlantı Hatası",
                            text: errMsg
                        });
                    }
                });
            });

            $('#btnConfirmSave').on('click', function () {
                var btn = $(this);
                var originalHtml = btn.html();

                Swal.fire({
                    title: "Soruları Aktarmak İstiyor musunuz?",
                    text: "Analiz edilen tüm sorular ve kanuni çözümleri seçilen kategoriye eklenecektir.",
                    icon: "question",
                    showCancelButton: true,
                    confirmButtonColor: "#28a745",
                    cancelButtonColor: "#6c757d",
                    confirmButtonText: "Evet, Veritabanına Ekle",
                    cancelButtonText: "İptal"
                }).then(function (result) {
                    if (!result.isConfirmed) return;

                    btn.prop('disabled', true).html('<span class="spinner-border spinner-border-sm mr-2"></span> Veritabanına Ekleniyor...');

                    $.ajax({
                        url: '<?= base_url("book-import/save"); ?>',
                        type: 'POST',
                        data: {
                            '<?= $this->security->get_csrf_token_name(); ?>': '<?= $this->security->get_csrf_hash(); ?>',
                            'category_id': $('#category_id').val(),
                            'exam_id': $('#exam_id').val(),
                            'badge': $('#badge').val()
                        },
                        dataType: 'json',
                        success: function (res) {
                            btn.prop('disabled', false).html(originalHtml);
                            if (res.error) {
                                Swal.fire({ icon: "error", title: "Hata", text: res.message });
                            } else {
                                Swal.fire({ icon: "success", title: "Başarılı!", text: res.message }).then(function () {
                                    window.location.href = res.redirect;
                                });
                            }
                        },
                        error: function (xhr, status, err) {
                            btn.prop('disabled', false).html(originalHtml);
                            Swal.fire({ icon: "error", title: "Hata", text: "Kayıt işlemi sırasında sunucu hatası oluştu." });
                        }
                    });
                });
            });
        });
    </script>
</body>

</html>
