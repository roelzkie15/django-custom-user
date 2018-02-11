from django.views.generic import TemplateView
from django.shortcuts import redirect

class BaseView(TemplateView):
    template_name = 'master/base.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            # Redirect to home page since this user is already authenticated
            return redirect('login')
        return super().dispatch(*args, **kwargs)
