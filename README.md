# gb_habr

# Stack:
- Python 3.9
- Django 4.1.1
- Bootstrap
- Postgres

# Запуск:
1. В директории `django/habr/` копируем файл `example.settings.py` в `settings.py` и меняем в нём настройки БД на своё окружение. 
2. Переходим в директорию django.
3. Устанавливаем зависимости Python:  
`pip install -r requirements.txt`
4. Запускаем сервер разработки:  
`python manage.py runserver`
5. В бразуере открываем наш сайт:
`http://127.0.0.1:8000`