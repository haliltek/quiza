# Quiza (Elite Quiz v2.3.9.1) — Sunucu Kurulum & Operasyon Kılavuzu

Bu belge, **Quiza (Elite Quiz v2.3.9.1)** sisteminin uzak Linux sunucu (`142.93.104.78`) üzerindeki Docker altyapısını, servis konfigürasyonlarını, bakım ve yedekleme operasyonlarını detaylandırmaktadır.

---

## 1. Sunucu Altyapısı & Servis Haritası

- **Sunucu IP:** `142.93.104.78`
- **İşletim Sistemi:** Ubuntu Linux (x86_64)
- **Konteynerleştirme:** Docker & Docker Compose
- **Proje Konumu:** `/opt/elitequiz`

### Kritik: Çoklu Sistem İzolasyon Kuralları
Sunucu üzerinde Quiza dışında 4 bağımsız sistem çalışmaktadır:
1. `portfolio-2025` (Port 3090)
2. `kizkiza_*` (Port 8092, MySQL, API)
3. `sharka-web` (Port 8091)
4. `pokebook-web` (Port 8090)

> [!CAUTION]
> **Asla Yapılmaması Gerekenler:**
> - `docker stop $(docker ps -aq)` veya `docker system prune -a --volumes` gibi tüm sunucuyu etkileyen komutlar **kesinlikle çalıştırılmamalıdır**.
> - Diğer servislerin kullandığı `3090`, `8090`, `8091`, `8092` portları veya MySQL portları ellenmemelidir.
> - Tüm Quiza işlemleri yalnızca `/opt/elitequiz` dizininde ve `elitequiz_*` container'ları üzerinde yürütülmelidir.

---

## 2. Docker Compose Servis Yapısı

Quiza üç adet izole Docker servisinden oluşur (`/opt/elitequiz/docker-compose.yml`):

| Servis Adı | Container Adı | İmaj / Taban | Bağlı Portlar | Açıklama |
|---|---|---|---|---|
| `elitequiz_db` | `elitequiz_db` | `mysql:8.0` | Dahili (3306) | Veritabanı motoru (`elite_quiz_db`) |
| `elitequiz_api` | `elitequiz_api` | `php:8.1-fpm` (Custom) | Dahili (9000) | PHP 8.1 FPM + GD + MySQLi + PDO |
| `elitequiz_webserver` | `elitequiz_webserver` | `nginx:alpine` | `0.0.0.0:8088->80` | Web sunucu, ters proxy, statik dosya sunucusu |

### Docker Ağı ve Birimleri (Volumes):
- **Ağ:** `elitequiz_net` (Bridge modunda, diğer sunucu ağlarından yalıtılmış)
- **Veritabanı Kalıcı Depolama:** `elitequiz_db_data` Docker Volume

---

## 3. Günlük Operasyon ve Bakım Komutları

Sunucuya bağlanma:
```bash
ssh root@142.93.104.78
cd /opt/elitequiz
```

### Servisleri Başlatma / Durdurma / Yeniden Başlatma:
```bash
# Arka planda başlatma
docker compose up -d

# Servisleri durdurma (veriler korunur)
docker compose down

# Yalnızca web sunucusunu yeniden başlatma (Nginx konfigürasyon değişikliğinde)
docker compose restart elitequiz_webserver

# Yalnızca PHP motorunu yeniden başlatma
docker compose restart elitequiz_api
```

### Logları Canlı Takip Etme:
```bash
# Tüm sistem logları
docker compose logs -f

# Sadece API (PHP) hata logları
docker compose logs -f elitequiz_api

# Sadece Nginx erişim ve hata logları
docker compose logs -f elitequiz_webserver
```

---

## 4. Veritabanı Yedekleme ve Geri Yükleme

### Manuel Yedek Alma:
```bash
docker exec elitequiz_db mysqldump -u elite_user -pelite_user_pass_2026 elite_quiz_db > /opt/elitequiz_backup_$(date +%Y%m%d).sql
```

### Yedeği Geri Yükleme:
```bash
docker exec -i elitequiz_db mysql -u elite_user -pelite_user_pass_2026 elite_quiz_db < /opt/elitequiz_backup_DOSYA_ADI.sql
```

---

## 5. Nginx ve PHP İnce Ayarları

1. **`output_buffering = On`**: CodeIgniter 3 session ve header yönlendirmeleri için zorunludur.
2. **`upload_max_filesize = 64M` & `post_max_size = 64M`**: Büyük soru görselleri, ses dosyaları ve dil paketlerinin sorunsuz yüklenebilmesi için ayarlanmıştır.
3. **`client_max_body_size 64M;`**: Nginx seviyesinde 413 Request Entity Too Large hatasını engeller.
4. **CodeIgniter URL Rewrite**:
   ```nginx
   location / {
       try_files $uri $uri/ /index.php?$query_string;
   }
   ```
