FROM php:8.1-fpm

RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libzip-dev \
    zip \
    unzip \
    curl \
    libonig-dev

RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j4 gd pdo pdo_mysql mysqli zip mbstring

RUN echo "output_buffering = On" > /usr/local/etc/php/conf.d/output-buffering.ini
RUN echo "upload_max_filesize = 64M" > /usr/local/etc/php/conf.d/uploads.ini
RUN echo "post_max_size = 64M" >> /usr/local/etc/php/conf.d/uploads.ini
RUN echo "memory_limit = 256M" >> /usr/local/etc/php/conf.d/uploads.ini
RUN echo "max_execution_time = 300" >> /usr/local/etc/php/conf.d/uploads.ini

WORKDIR /var/www/html
