"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup_view, name='signup'),  # URL d'inscription
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL de connexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de déconnexion
    path('', accounts_views.home, name='home'),  # URL de la page d'accueil
]