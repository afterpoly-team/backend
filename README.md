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
    {
        "event_date": "21-04-16"
    },
    {
        "event_date": "21-04-17"
    },
    {
        "event_date": "21-04-18"
    }
]
```
