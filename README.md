# Site

Описание проекта:

Кулинарный форум с регистрацией пользователей и реализацией API

# Инстументы разработки:

Стек:

+ Django 3.1, Django REST Framework 3.12, and Python 3.12

+ JWT Web Token auth

+ Signup

+ sqlite3
  

# Разработка
1) Клонировать репозиторий
```
git clone https://github.com/VR48hyukh/config.git
```
2) Создать виртульное окружение 
```
cd pythonProject3

python -m venv venv
```

3) Активировать виртуальное окружение
   
 Linux
```
source venv/bin/activate
```
 Windows 
```
./venv/Scripts/activate
```
4) Установить зависимости:
```
pip install -r req.txt
```
5) Выполнить команду для выполнения миграций 
```
python manage.py migrate
```
6) Создать суперпользователя
```
python manage.py createsuperuser
```
7) Запустить сервер
```
python manage.py runserver
```

# Ссылки 

Админ-панель
```
http://127.0.0.1:8000/admin/
```

```
http://127.0.0.1:8000/api/v1/token/
```

```
http://127.0.0.1:8000/api/v1/token/refresh/
```

```
http://127.0.0.1:8000/api/v1/token/verify/
```

```
http://127.0.0.1:8000/api/v1/home/
```


```
http://127.0.0.1:8000/api/v1/recipe/
```


```
http://127.0.0.1:8000/api/v2/post/
```


```
http://127.0.0.1:8000/api/v2/comment/
```


```
http://127.0.0.1:8000/api/v2/about/1
```






















