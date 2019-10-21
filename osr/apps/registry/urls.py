from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.SportTypeListView.as_view(), name='registry'),

    path('sport-type/', include([
        path('', views.SportTypeListView.as_view(), name='sport-type-list'),
        path('<int:pk>/', views.SportTypeDetailView.as_view(), name='sport-type-detail'),
        path('create/', views.SportTypeCreateView.as_view(), name='sport-typecreate'),
        path('<int:pk>/update/', views.SportTypeUpdateView.as_view(), name='sport-type-update'),
        path('<int:pk>/delete/', views.SportTypeDeleteView.as_view(), name='sport-type-delete'),
    ])),

]
