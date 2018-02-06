from django.urls import path

from .views import Signup, UserDetail, UserUpdate

app_name = 'account'

urlpatterns = [
    path('sign-up/', Signup.as_view(), name='sign-up'),
    path('my-account', UserDetail.as_view(), name='detail'),
    path('my-account/edit-profile', UserUpdate.as_view(), name='edit')
]
