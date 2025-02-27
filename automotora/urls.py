from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from autos.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
