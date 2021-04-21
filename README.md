# backend

This is a backend of AfterPoly web-application

# instructions

How to setup an environment to use this backend-server using command-line:

1. Make sure you have python3.\* installed:
   `python --version`
2. Install virtual environment (this is **pipenv**, but you can choose your own):
    - go to directory you cloned this repository
    - `pip install pipenv`
3. Go to **pipenv** shell and install all packages:
    - `pipenv shell`

    option 1:

    - `pipenv install -r /path/to/requirements.txt`

    option 2:

    - `pipenv install Django==3.1.7`
    - `pipenv install djangorestframework==3.12.4`
    - `pipenv install django-cors-headers==3.7.0`
    - `pipenv install django-modeltranslation==0.16.2`
    - `pipenv install Pillow==8.2.0`
    - `pipenv install django-filter==2.4.0`
      ...
      etc depends on what inside the requirements

# usage

Now you must be able to work with server, using such commands:

-   `python manage.py runserver` - starts a server

[

-   `python manage.py makemigrations` - sets your bd with migrations
-   `python manage.py migrate` - makes migrations
    ] -> use this comannds after model-modigying

-   `python manage.py createsuperuser` - creates an admin user

# template for dateField (as JSON)

```
[
    "event_date": "21-04-16",
    "event_date": "21-04-17",
    "event_date": "21-04-18"
]
```

# how to use query params

in the url, after '?' sign, you can add the filtering param,
as an example (many params are concatenated by '&' sign, NO SPACES ALLOWED):

-   Pagination:
    `.../?page_size=1`->sets page size, as you can guess
    (http://127.0.0.1:8000/ru/api/places/?page_size=1 OR http://127.0.0.1:8000/ru/api/places/?page=2&page_size=1 e.t.c)
    `.../?page=2`-> sets the page you see
    (http://127.0.0.1:8000/ru/api/online-events/?page=2&page_size=1 e.t.c)

-   Filtering:
    http://127.0.0.1:8000/ru/api/real-life-events/?tags=Концерт OR http://127.0.0.1:8000/ru/api/real-life-events/?tags=Концерт&tags=Фильм&tags=Обучение e.t.c


# style
Python Coding Guidelines
https://drive.google.com/file/d/1lFBLbd9vsRdgX7dXUpUzQzrH0mmwJO0N/view?usp=sharing

