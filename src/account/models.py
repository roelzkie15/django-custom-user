from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.dispatch import receiver

from allauth.account.signals import  user_signed_up

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
