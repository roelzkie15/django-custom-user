from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect,render

from allauth.account import app_settings
from allauth.account.signals import  user_signed_up
from allauth.account.utils import perform_login, send_email_confirmation
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.models import EmailAddress as s_emails
from allauth.socialaccount.signals import pre_social_login
from allauth.utils import get_user_model

class UserManager(BaseUserManager):
    def _create_user(self, email, username=None, is_admin=False, is_staff=False, password=None):
        'Method for actual creation of a user'

        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_admin=is_admin,
            is_staff=is_staff
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None):
        'Create a simple user'
        return self._create_user(email=email, username=username, password=password)

    def create_staffuser(self, email, username=None, password=None):
        'Create a staff user'
        return self._create_user(email=email, username=username, is_staff=True, password=password)

    def create_superuser(self, email, username=None, password=None):
        'Create a super user'
        return self._create_user(
            email=email, username=username, is_admin=True,
            is_staff=True, password=password
        )

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

    def get_full_name(self):
        return f'{self.name}'

    def get_short_name(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        'Does the user have a specific permission?'
        return True

    def has_module_perms(self, app_label):
        'Does the user have permissions to view the app `app_label`?'
        return True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def has_staff_perm(self):
        'Is the user a member of staff?'
        return self.is_staff

    @property
    def has_active_perm(self):
        'Is the user active?'
        return self.is_active

    @property
    def has_admin_perm(self):
        'Is the user is super admin?'
        return self.is_admin

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    user.is_active = True # Only for allauth account to avoid inactive user authentication.
    user.save()

@receiver(pre_social_login)
def pre_social_login_(sender, request, sociallogin, **kwargs):
    '''
    Resolve issue of existing email address. When signing up a social account with the existing
    email address it will logged the existing user. And for security hole issue the account
    will not successfully logged if their given email address are not verified.
    To verify ownership of email this function will automatically send a verification link
    to the given email and only legit user can access the said account.
    :param sender:
    :param request:
    :param sociallogin:
    :param kwargs:
    :return:
    '''

    email = sociallogin.account.extra_data['email']
    _user = get_user_model()
    users = _user.objects.filter(email=email)
    _s_emails = s_emails.objects.filter(email=email)
    e_existing = _s_emails.exists()
    u_existing = users.exists()

    if u_existing :
        if e_existing:
            if _s_emails[0].verified:
                perform_login(request, users[0], app_settings.EMAIL_VERIFICATION)
                raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL))

        send_email_confirmation(request, users[0])
        raise ImmediateHttpResponse(render(request, 'account/verification_sent.html', {}))
