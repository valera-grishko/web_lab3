# web_lab3

## Лабораторна робота №3
### Виконав: Гришко Валерій Валерійович КВ-21мп
### https://docs.google.com/document/d/1S-baJcUogJylccTN3cNbxbKUDpica_BqCB-v95vySnQ/edit


## Install requirements
```pip install -r requirements.txt```
## Run server
```python manage.py runserver```
## Run with websockets
```daphne blog.asgi:application```
## Run celery queues
```celery -A blog worker --loglevel=INFO -Q slow -n slow_worker -P eventlet```

```celery -A blog worker --loglevel=INFO -Q fast -n fast_worker -P eventlet```
## Create superuser
```python manage.py createsuperuser```
## Create migrations
```python manage.py makemigrations```
## Migrate
```python manage.py migrate```