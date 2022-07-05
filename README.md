# Как запустить это дело

## Backend
1. Необходимо установить ``Python 3.10.4`` (желательно эту версию)
2. Создаем и подключаем виртуальное окружение Python внутри папки ``Backend``
   1. В ``Linux``:
      1. ``python -m venv venv``, при необходимости скачиваем все необходимые пакеты
      2. Чтобы подключить ``source venv/bin/activate``
   2. В ``Windows``:
      1. ``python -m venv venv``
      2. Чтобы подключить ``venv/bin/activate``
3. Теперь имортируем все необходимые пакеты из файла ``requirements.txt`` командой: ``pip install -r requirements.txt ``  
P.s. при возникновении проблем установки пакетов данной командой, открываем файл и вручную командой ``pip install <имя пакета>`` импортируем каждый пакет.
4. Создаем в папке ``court_cases_backend`` файл ``password.py`` следующей структуры:
```
SECRET_KEY = 'django-insecure--<куча символов>'

db_ip = '127.0.0.1'
db_port = '5432'
db_name = '<имя базы>'
db_login = '<имя пользователя>'
db_password = '<пароль>'
```  
5. Запускаем миграцию БД с корня папки ``court_cases_backend`` командами  ``python manage.py makemigrations`` и ``python manage.py migrate``
6. Создаем суперпользователя командой ``python manage.py createsuperuser`` и вводим все запрашиваемые данные
7. Запускаем сервер командой ``python manage.py runserver``
8. Для доступа к админке проходим по ссылке ``127.0.0.1:8000/admin`` и логинимся под суперпользователем.
9. Для доступа к API есть следующие пути (все они прописаны дополнительно в рабочем пространстве Postman):
```
users/ ['GET']
users/current-detail/ ['GET']
users/<str:pk>/ ['GET']
courts/ ['GET']
courts/create/ ['POST']
courts/<str:pk>/ ['GET']
courts/<str:pk>/update/ ['PUT']
courts/<str:pk>/delete/ ['DELETE']
api-token-auth/ ['POST'] 
```