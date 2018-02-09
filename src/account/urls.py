from django.urls import path

from .views import activate, EmailVerificationNotice, Signup, UserDetail, UserUpdate

app_name = 'account'

urlpatterns = [
    path('sign-up', Signup.as_view(), name='sign-up'),
    path('verification-notice', EmailVerificationNotice.as_view(), name='notice'),
    path('my-account/activate/<str:uid>/<str:token>', activate, name='activate'),
    path('my-account', UserDetail.as_view(), name='detail'),
    path('my-account/edit-profile', UserUpdate.as_view(), name='edit')
]
