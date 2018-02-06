# django-custom-user

## Installation


Dependencies
- python3.x and higher
- Get [pipenv](https://docs.pipenv.org/)_(I recommend this)_ for virtualenvs and package manager.

How to use?
- clone repository
- `$ pipenv install `
- `$ python manage.py makemigrations`
- `$ python manage.py migrate`
- Create a super user by executing `$ python manage.py createsuperuser`
- `$ cd src && python manage.py runserver`
- open url http://localhost:8000

## Current Feature
- Custom user model derived from AbstractBaseUser
- Custom user model create and change form function
- User authentication on template
- Change password and reset with email validation using [SendGrid](https://sendgrid.com/)

## Roadmap
 - Material Design
 - Account verification when sign up via email
 - Social authentication
 