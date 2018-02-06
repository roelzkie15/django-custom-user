from django.urls import path

from .views import Signup, UserDetail

app_name = 'account'

urlpatterns = [
    path('sign-up/', Signup.as_view(), name='sign-up'),
    path('my-account', UserDetail.as_view(), name='my-account')
]
