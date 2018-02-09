from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    def _create_user(self, email, name=None, is_admin=False, is_staff=False, is_active=False, password=None):
        'Method for actual creation of a user'

        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_admin=is_admin,
            is_staff=is_staff,
            is_active=is_active
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name=None, password=None):
        'Create a simple user'
        return self._create_user(email=email, name=name, password=password)

    def create_staffuser(self, email, name=None, password=None):
        'Create a staff user'
        return self._create_user(email=email, name=name, is_staff=True, password=password)

    def create_superuser(self, email, name=None, password=None):
        'Create a super user'
        return self._create_user(
            email=email, name=name, is_admin=True,
            is_staff=True, is_active=True, password=password
        )

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=150)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.email}'

    def get_full_name(self):
        return f'{self.name}'

    def get_short_name(self):
        return f'{self.name}'

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
