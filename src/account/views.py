from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import User
from .forms import UserCreationForm

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/sign-up.html'

class UserDetail(TemplateView):
    template_name = 'account/my-account.html'


