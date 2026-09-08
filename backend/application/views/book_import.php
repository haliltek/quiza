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
            box-shadow: 0 4px 8px rgba(0,0,0,.05);
        }
        .preview-box {
            max-height: 600px;
            overflow-y: auto;
        }
        .q-card {
            border-left: 4px solid #3abaf4;
            margin-bottom: 15px;
            background: #fdfdff;
        }
        .solution-box {
            background-color: #f4f6f9;
            border-radius: 6px;
            padding: 10px 14px;
            font-size: 0.9rem;
            color: #3e445b;
            border-left: 3px solid #28a745;
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
                        <div class="row">
                            <div class="col-12">
                                <div class="card source-card">
                                    <div class="card-header d-flex justify-content-between">
                                        <h4><em class="fas fa-magic mr-2 text-primary"></em> Akıllı Kitap & PDF Analiz Motoru</h4>
                                        <span class="badge badge-success"><em class="fas fa-check-circle mr-1"></em> Scribd & PDF Destekli</span>
                                    </div>
                                    <div class="card-body">
                                        <div class="alert alert-light border">
                                            <em class="fas fa-info-circle text-primary mr-2"></em>
                                            Bu sayfadan <strong>Scribd kitap linklerini</strong> (örn: <code>https://www.scribd.com/document/822952525/...</code>), doğrudan <strong>PDF web linklerini</strong> veya bilgisayarınızdaki bir <strong>PDF soru bankasını</strong> girerek tüm soruları, şıkları, doğru cevapları ve detaylı çözümleri otomatik olarak çıkarıp sisteme ekleyebilirsiniz.
                                        </div>

                                        <form id="importForm" enctype="multipart/form-data">
                                            <input type="hidden" name="<?= $this->security->get_csrf_token_name(); ?>" value="<?= $this->security->get_csrf_hash(); ?>">

                                            <div class="row">
                                                <div class="form-group col-md-8">
                                                    <label class="font-weight-bold">Kitap / Soru Bankası URL Adresi (Scribd veya Doğrudan PDF):</label>
                                                    <div class="input-group">
                                                        <div class="input-group-prepend">
                                                            <div class="input-group-text"><em class="fas fa-link"></em></div>
                                                        </div>
                                                        <input type="url" name="url" id="doc_url" class="form-control" placeholder="https://www.scribd.com/document/... veya https://.../sorular.pdf">
                                                    </div>
                                                    <small class="form-text text-muted">Scribd doküman linki veya doğrudan internetteki PDF linki.</small>
                                                </div>

                                                <div class="form-group col-md-4">
                                                    <label class="font-weight-bold">VEYA Doğrudan PDF Dosyası Yükle:</label>
                                                    <input type="file" name="pdf_file" id="pdf_file" class="form-control" accept=".pdf">
                                                </div>
                                            </div>

                                            <div class="row">
                                                <div class="form-group col-md-4">
                                                    <label class="font-weight-bold">Hedef Kategori:</label>
                                                    <select name="category_id" id="category_id" class="form-control select2">
                                                        <?php foreach ($categories as $cat) { ?>
                                                            <option value="<?= $cat->id; ?>" <?= ($cat->id == 11 || $cat->id == 3) ? 'selected' : ''; ?>>
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
                                                    <small class="form-text text-muted">Seçilirse sorular doğrudan bu deneme sınavına da eklenir.</small>
                                                </div>
                                            </div>

                                            <div class="form-group mt-2">
                                                <button type="button" id="btnPreview" class="btn btn-primary btn-lg shadow-sm">
                                                    <em class="fas fa-search mr-2"></em> Kitabı İndir, Analiz Et ve Önizle
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
                                            <em class="fas fa-check-double mr-1"></em> Kitap içeriği çözümlendi! Aşağıda tespit edilen ilk sorular, şıkları, doğru cevapları ve detaylı kanuni çözümleri önizlenmektedir. <strong>"Tüm Soruları Veritabanına Aktar"</strong> butonuna basarak tüm soruları canlı sisteme kaydedebilirsiniz.
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

                if (!url && !file) {
                    Swal.fire({
                        icon: "warning",
                        title: "Eksik Bilgi",
                        text: "Lütfen bir kitap/PDF linki girin veya bilgisayarınızdan PDF dosyası seçin."
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
                            listHtml += '<h6 class="text-primary font-weight-bold mb-0">Soru ' + (idx + 1) + '</h6>';
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
                                listHtml += '<strong><em class="fas fa-lightbulb text-warning mr-1"></em> Detaylı Çözüm / Açıklama:</strong><br>';
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
                        Swal.fire({
                            icon: "error",
                            title: "Bağlantı Hatası",
                            text: "Sunucu isteği işlerken hata oluştu: " + err
                        });
                    }
                });
            });

            $('#btnConfirmSave').on('click', function () {
                var btn = $(this);
                var originalHtml = btn.html();

                Swal.fire({
                    title: "Soruları Aktarmak İstiyor musunuz?",
                    text: "Analiz edilen tüm sorular ve çözümleri seçilen kategoriye eklenecektir.",
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
