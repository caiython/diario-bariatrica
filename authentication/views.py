from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class LoginView(FormView):
    template_name = "auth/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response({'form': form})


class LogoutView(TemplateView):
    template_name = "auth/logout.html"

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class SignupView(TemplateView):
    template_name = "auth/signup.html"
