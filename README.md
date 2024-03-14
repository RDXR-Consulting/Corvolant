# Corvolant

Это приложение, мультитул для проведения аудита безопасности веб-приложений и приложений. Агрегатор для различных инструментов тестирования безопасности сайта или приложения. Оно предназначено для проверки безопасности приложений и систем.


## Features

- Фича 11111112


## Documentation

[Documentation](https://linktodocumentation)


## Screenshots

![Screen](https://github.com/RDXR-Consulting/Corvolant/assets/104996756/cefd055f-83bf-4fbb-8ce9-3bf703d2fc02)


## Установка
```bash
sudo systemctl start postgresql
sudo service postgresql start
sudo passwd postgres -> "12345"
su -l postgres -> "12345"
psql
CREATE USER crvlhost WITH password 'crvlpass';
CREATE DATABASE crvldb;
\c crvldb
CREATE TABLE keys( id SERIAL PRIMARY KEY, lang CHARACTER VARYING(30), register INTEGER );
GRANT ALL PRIVILEGES ON DATABASE crvldb to crvlhost;
GRANT ALL ON keys TO crvlhost;
\q
exit
clear
```

## FAQ

#### 1) На каких OS доступна программа?

Corvolant доступен на Windows


## Authors

- [@radixiura](https://github.com/radixiura)
- [@DunastyCode](https://www.github.com/dunastycode)
- [@backDoora](https://github.com/backDoora)


## Feedback

Если у вас есть какие-либо отзывы, пожалуйста, свяжитесь с нами по адресу crvl.com

