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
   - `pipenv install django`
   - `pipenv install djangorestframework`
   - `pipenv install django-cors-headers`

# usage

Now you must be able to work with server, using such commands:

- `python manage.py runserver` - starts a server

[
- `python manage.py makemigrations` - sets your bd with migrations
- `python manage.py migrate` - makes migrations
  ] -> use this comannds after model-modigying

- `python manage.py createsuperuser` - creates an admin user
