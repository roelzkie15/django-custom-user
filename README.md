# django-custom-

### Current Feature
- Custom user model derived from AbstractBaseUser with email as username field.
- Custom user model create and change form function for admin.
- Authentication and edit user profile in the template.
- Change password and reset with email validation using [SendGrid](https://sendgrid.com/).
- Account verification when sign up via email SendGrid.
- Social authentication (GitHub, Google+, Twitter, Facebook)
- Linking of multiple social account to existing email address (django-allauth)
- Material Design

Demo link [here](https://django-custom-user.herokuapp.com/).

## Installation


### Dependencies
- python3.x and higher
- Get [pipenv](https://docs.pipenv.org/)_(I recommend this)_ for virtualenvs and package manager.

### Installation

- Clone repository
- `$ pipenv install`
- `$ python manage.py makemigrations && python manage.py migrate && python manage.py runserver`
- To create superuser `$ python manage.py createsuperuser`
- Open [localhost](http://127.0.0.1:8000) url.

### Creating Social Application

#### Github

App registration to get your key and secret [here](https://github.com/settings/applications/new). 

Add development callback `http://127.0.0.1:8000/accounts/github/login/callback/`

Use your production domain name for live site  `http://{{ domain_name }}/accounts/github/login/callback/`

#### Google

App registration to get your key and secret [here](https://console.developers.google.com/apis/credentials). 
   
   -  Click **Create Credentials** drop button and choose **OAuth Client ID**.
   -  Select web application for application type radio button selection.
   -  Add name and under Authorized redirect URIs include. `http://127.0.0.1:8000/accounts/google/login/callback` _(Google can provide multiple redirect uris, so you can include as many as you may need.)_
   - Click create and you can get your key and secret.


Use your production domain name for live site.

### Twitter

App registration to get your key and secret [here](https://apps.twitter.com/app/new). 
   
   -  Create an app
   -  Add this `http://127.0.0.1:8000/accounts/twitter/login/callback/` as your for callback uri  
   - Twitter doesnt accept localhost domain name `http://localhost:8000/accounts/twitter/login/callback/`

Because this application always required valid email for authentication process it may let you verified the given email 
for twitter and in order to get the email of your twitter:

   - After creating application click the newly created app and go to **Permissions** tab,
   below check the option for Request email address from users. Of course twitter is very strict it this regard and
   and in order to do so you must Privacy Policy URL and Term of Services URL then you are good to go.
   - One more thing is you may need to check _Enable Callback Locking (It is recommended to enable callback locking to ensure apps cannot overwrite the callback url)_ option.

Use your production domain name for live site.

### Facebook

App registration to get your key and secret [here](https://developers.facebook.com/apps/). 
  
  - Add a new app, enter the required fields and click __Create App ID__
  - Add product and choose Facebook login
  - Ignore the Quickstart and go to the Settings of Facebook logic category.
  - Add `http://127.0.0.1:8000/accounts/facebook/login/callback/` in the redirect URIs _(You can add multiple uris)_. Save Changes
  - In order to make your facebook app live you must also provide Privacy Policy URL and Term of Services URL
  under the __Settings > Basic__ side menu.
  - Go to app review and make your app public. You will see the Approved items is enabled then your are good to go.
  
Use your production domain name for live site.
  

## Registering Social Account

First go to administrator login and enter your credentials for supersuser.
    
   - Click the __Sites__ and change the example.com domain name to localhost for development or use your production domain name.
   - Back to home page and under the `Social Account > Social applications` add a social application
   - Enter provider, name, client id and secret and select a chosen sites then click save. 
     
Great example can be found here by [Will Vincent](https://github.com/wsvincent) [Django Allauth Tutorial](https://wsvincent.com/django-allauth-tutorial).  

## Acknowledgement

Will Vincent author of [Django for beginners](djangoforbeginners.com)

Raymond Penners author of [django-allauth](https://github.com/pennersr/django-allauth)
