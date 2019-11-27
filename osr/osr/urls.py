from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registry/', include('apps.registry.urls'), name="registry"),
    path('auth/', include('apps.account.urls'), name="auth")
    #path('', include(), name="index")
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
