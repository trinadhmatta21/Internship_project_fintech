"""
URL configuration for simple_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# simple_project/urls.py
from django.contrib import admin
from django.urls import path
from userauth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('manage_ipo/', views.manage_ipo_view, name='manage_ipo'),
    path('manage_ipo/register/', views.register_ipo_view, name='register_ipo'),
    path('manage_ipo/edit/<int:ipo_id>/', views.edit_ipo_view, name='edit_ipo'),  # New
    path('manage_ipo/delete/<int:ipo_id>/', views.delete_ipo_view, name='delete_ipo'),
    path('userside/', views.user_side, name='userside'),
    path('forgot/', views.forgot_password_view, name='forgot'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
