from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.RegitryTemplateView.as_view(), name='registry'),

    path('sport-type/', include([
        path('', views.SportTypeListView.as_view(), name='sport-type-list'),
        path('<int:pk>/', views.SportTypeDetailView.as_view(), name='sport-type-detail'),
        path('create/', views.SportTypeCreateView.as_view(), name='sport-type-create'),
        path('<int:pk>/update/', views.SportTypeUpdateView.as_view(), name='sport-type-update'),
        path('<int:pk>/delete/', views.SportTypeDeleteView.as_view(), name='sport-type-delete'),
    ])),

    path('coach/', include([
        path('', views.CoachListView.as_view(), name='coach-list'),
        path('<int:pk>/', views.CoachDetailView.as_view(), name='coach-detail'),
        path('create/', views.CoachCreateView.as_view(), name='coach-create'),
        path('<int:pk>/update/', views.CoachUpdateView.as_view(), name='coach-update'),
        path('<int:pk>/delete/', views.CoachDeleteView.as_view(), name='coach-delete'),
    ])),

    path('parent/', include([
        path('', views.ParentListView.as_view(), name='parent-list'),
        path('<int:pk>/', views.ParentDetailView.as_view(), name='parent-detail'),
        path('create/', views.ParentCreateView.as_view(), name='parent-create'),
        path('<int:pk>/update/', views.ParentUpdateView.as_view(), name='parent-update'),
        path('<int:pk>/delete/', views.ParentDeleteView.as_view(), name='parent-delete'),
    ])),

    path('sportsman/', include([
        path('', views.SportsmanListView.as_view(), name='sportsman-list'),
        path('<int:pk>/', views.SportsmanDetailView.as_view(), name='sportsman-detail'),
        path('create/', views.SportsmanCreateView.as_view(), name='sportsman-create'),
        path('<int:pk>/update/', views.SportsmanUpdateView.as_view(), name='sportsman-update'),
        path('<int:pk>/delete/', views.SportsmanDeleteView.as_view(), name='sportsman-delete'),
    ])),
]
