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
- Open [localhost](http://127.0.0.1:8000) url.

## Current Feature
- Custom user model derived from AbstractBaseUser with email as username field.
- Custom user model create and change form function for admin.
- Authentication and edit user profile in the template.
- Change password and reset with email validation using [SendGrid](https://sendgrid.com/).
- Account verification when sign up via email SendGrid.
 
## Roadmap
 - Social authentication (Github, Google+, Twitter, Facebook)
 - Material Design
 