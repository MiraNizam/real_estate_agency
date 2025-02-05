# Сайт риэлторского агентства

Сайт для агентства недвижимости. 
  - Главная страница для поиска квартир с фильтрами. 
![main_page](main_page.png)
  - Административная панель для навигации по базе, внесения данных о недвижимости и владельцах. 
      * Карточка недвижимости
      * Карточка собственника
      * Карточка замечаний по объявлениям

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

    Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

