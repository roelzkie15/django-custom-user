from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import UserSignupForm, UserUpdateForm
from .models import User
from .tokens import account_activation_token


from django.template.loader import render_to_string

class Signup(CreateView, UserPassesTestMixin):
    form_class = UserSignupForm
    success_url = reverse_lazy('account:notice')
    template_name = 'account/sign-up.html'

    def form_valid(self, form):

        # Save the provided password in hashed format
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()

        # Prepare email activation content
        current_site = get_current_site(self.request)
        subject = 'Activate your account'
        message = render_to_string('account/account-activation-email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': account_activation_token.make_token(user),
        })

        user.email_user(subject, message)

        return super().form_valid(form)

    def test_func(self):
        return not self.user.is_authenticated

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

class EmailVerificationNotice(TemplateView):
    template_name = 'account/email-verification-notice.html'

def activate(request, uid, token):
    '''
    Explicitly activate newly registered user account
    :param request:
    :param uid64: hashed id of the user
    :param token: token provided in the verification link
    :return:
    '''
    try:
        _uid = force_text(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=_uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account/account-verification-invalid-notice.html')



