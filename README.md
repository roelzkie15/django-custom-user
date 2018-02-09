# django-custom-user

## Installation


Dependencies
- python3.x and higher
- Get [pipenv](https://docs.pipenv.org/)_(I recommend this)_ for virtualenvs and package manager.

How to use?
- Clone repository
- `$ pipenv install `
- `$ cd src && python manage.py makemigrations && python manage.py migrate && python manage.py runserver`
- To create superuser `$ python manage.py createsuperuser`
- Open url http://localhost:8000

## Current Feature
- Custom user model derived from AbstractBaseUser
- Custom user model create and change form function
- User authentication on template
- Change password and reset with email validation using [SendGrid](https://sendgrid.com/)
- Account verification when sign up via email
 
## Roadmap
 - Social authentication
 - Material Design
 