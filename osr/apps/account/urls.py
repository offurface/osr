from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.LoginFormView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

