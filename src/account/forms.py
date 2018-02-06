from django import forms
from django.forms import widgets
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    '''
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    '''
    password1 = forms.CharField(label='Password', max_length=60, widget=widgets.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', max_length=60, widget=widgets.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name')

    def clean_password2(self):
        # Confirm if given password matched.
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    '''
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    '''
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'is_admin', 'is_staff', 'is_active')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserUpdateForm(forms.ModelForm):
    '''
    A form for updating users in the non-admin template.
    Includes only basic fields
    '''

    class Meta:
        model = User
        fields = ('email', 'name')