from django.urls import path, include, re_path
from django.contrib.auth import views

urlpatterns = [
    path('', views.LoginView.as_view(template_name='account/login.html'), name="login")

]

