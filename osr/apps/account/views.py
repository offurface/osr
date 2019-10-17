from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "account/login.html"
    success_url = "registry/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
