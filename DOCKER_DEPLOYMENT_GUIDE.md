# Elite Quiz v2.3.8 - Sunucu Kurulum Rehberi (Docker - 142.93.104.78)

Bu rehber, **142.93.104.78** sunucusundaki mevcut Docker konteynerlerine dokunmadan, Elite Quiz Admin Panel & REST API backend'ini bağımsız ve izole bir şekilde nasıl çalıştıracağınızı açıklar.

---

## 1. Mimari Mimarisi (Docker Containers)

Sunucuda çalışacak servisler:
1. **`elitequiz_db`**: MySQL 8.0 veritabanı konteyneri.
2. **`elitequiz_api`**: PHP 8.1-FPM konteyneri (CodeIgniter 3 çalıştırmak için gerekli tüm eklentiler yüklü).
3. **`elitequiz_webserver`**: Nginx web sunucusu (Port `8088` üzerinden dış dünyaya açık, istenirse Nginx Reverse Proxy ile domain bağlanabilir).

---

## 2. Hazırlanan Docker Yapılandırması

### A. `docker-compose.yml`
```yaml
version: '3.8'

services:
  elitequiz_db:
    image: mysql:8.0
    container_name: elitequiz_db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: elite_quiz_root_pass_2026
      MYSQL_DATABASE: elite_quiz_db
      MYSQL_USER: elite_user
      MYSQL_PASSWORD: elite_user_pass_2026
    volumes:
      - elitequiz_db_data:/var/lib/mysql
    networks:
      - elitequiz_net

  elitequiz_api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: elitequiz_api
    restart: always
    volumes:
      - ./backend:/var/www/html
    networks:
      - elitequiz_net

  elitequiz_webserver:
    image: nginx:alpine
    container_name: elitequiz_webserver
    restart: always
    ports:
      - "8088:80"
    volumes:
      - ./backend:/var/www/html
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - elitequiz_api
      - elitequiz_db
    networks:
      - elitequiz_net

networks:
  elitequiz_net:
    driver: bridge

volumes:
  elitequiz_db_data:
```

### B. `Dockerfile` (PHP FPM Custom Image)
```dockerfile
FROM php:8.1-fpm

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libzip-dev \
    zip \
    unzip \
    curl \
    libonig-dev

# PHP eklentilerini derle ve etkinleştir
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mysqli zip mbstring

# ob_start() ve performans ayarları
RUN echo "output_buffering = On" > /usr/local/etc/php/conf.d/output-buffering.ini
RUN echo "upload_max_filesize = 64M" > /usr/local/etc/php/conf.d/uploads.ini
RUN echo "post_max_size = 64M" >> /usr/local/etc/php/conf.d/uploads.ini

WORKDIR /var/www/html
```

### C. `nginx.conf` (CodeIgniter 3 Nginx Config)
```nginx
server {
    listen 80;
    server_name localhost;
    root /var/www/html;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass elitequiz_api:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

---

## 3. Kurulum ve Çalıştırma Adımları

1. **Sunucuya Bağlanma**:
   ```bash
   ssh root@142.93.104.78
   ```

2. **Proje Klasörüne Gitme / Oluşturma**:
   ```bash
   mkdir -p /opt/elitequiz
   cd /opt/elitequiz
   ```

3. **PHP Dosyalarını Çıkarma**:
   `PHP CODE 2.3.8.zip` içerisindeki dosyalar `/opt/elitequiz/backend/` dizinine çıkarılır.

4. **Docker Konteynerlerini Başlatma**:
   ```bash
   docker-compose up -d --build
   ```

5. **Kurulum Sihirbazını Tamamlama**:
   Tarayıcınızdan `http://142.93.104.78:8088` adresine gidin.
   - **DB Host**: `elitequiz_db`
   - **DB Name**: `elite_quiz_db`
   - **DB User**: `elite_user`
   - **DB Pass**: `elite_user_pass_2026`
   - **Varsayılan Giriş**: `admin` / `admin123`
