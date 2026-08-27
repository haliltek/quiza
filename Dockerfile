FROM php:8.1-fpm

# System dependencies
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libzip-dev \
    zip \
    unzip \
    curl \
    libonig-dev

# Install PHP extensions
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mysqli zip mbstring

# Output buffering and upload limits for CodeIgniter 3
RUN echo "output_buffering = On" > /usr/local/etc/php/conf.d/output-buffering.ini
RUN echo "upload_max_filesize = 64M" > /usr/local/etc/php/conf.d/uploads.ini
RUN echo "post_max_size = 64M" >> /usr/local/etc/php/conf.d/uploads.ini

WORKDIR /var/www/html
