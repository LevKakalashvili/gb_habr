# gb_habr

# Структура проекта:
- django/articles/templates: html шаблоны дизайна
- django/: приложение

# Stack:
- Python 3.9
- Django 4.1.1
- Bootstrap
- Postgres 14

# Установка:
1. В директории `django/config/` копируем файл `example.settings.py` в `settings.py` и меняем в нём настройки БД на своё окружение. 
2. Переходим в директорию django.
3. Устанавливаем зависимости Python:  
`pip install -r requirements.txt`
4. Выполняем миграцию БД:
`python manage.py migrate`

# Запуск: 
1. Запускаем сервер разработки:  
`python manage.py runserver`
2. В бразуере открываем наш сайт:
`http://127.0.0.1:8000`
