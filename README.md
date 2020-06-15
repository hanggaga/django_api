# django_api

## Requirement
- python latest version [Python](https://www.python.org/)
- git latest version [Git](https://git-scm.com/)
### Clone Repository
```
$ git clone https://github.com/hanggaga/django_api.git
```
### Install python package
```
$ pip install -r requirements.txt
```
### Creating an admin user
```
$ python manage.py createsuperuser
```
### The development server
```
$ python manage.py migrate
$ python manage.py runserver
```
1. Login at http://127.0.0.1:8000/admin/
2. Create Applications http://127.0.0.1:8000/oauth/applications/
Reference:
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django OAuth Toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html)