from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('sport-type/', include([
        path('', views.SportTypeView.as_view(), name='sport-type-list'),
        path('<int:pk>/', views.SportTypeDetailView.as_view(), name='sport-type-detail'),
        path('create/', views.SportTypeCreateView.as_view(), name='sport-typecreate'),
        #path('<int:id>/update/', views..as_view(), name='sport-type-update'),
        #path('<int:id>/delete/', views..as_view(), name='sport-type-delete'),
    ])),

]
