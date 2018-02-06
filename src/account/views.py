from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .models import User
from .forms import UserCreationForm, UserUpdateForm

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/sign-up.html'

class UserDetail(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'account/my-account.html'

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('account:detail')
    template_name = 'account/edit-profile.html'

    def get_object(self, queryset=None):
        'Get only logged user'
        return self.request.user



