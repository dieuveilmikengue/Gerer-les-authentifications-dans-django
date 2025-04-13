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
from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from accounts import views as accounts_views
# from django.contrib.auth.views import LogoutView
# from accounts.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', accounts_views.signup_view, name='signup'),  # URL d'inscription
    # path('login/', auth_views.LoginView.as_view(next_page='home'), name='login'),  # URL de connexion
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Redirection après déconnexion
    # path('', accounts_views.home, name='home'),  # URL de la page d'accueil
    
    # # Password change views
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # # Password reset views
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # #Profil
    # path('profile/', accounts_views.profile, name='profile'),  # Profile

    path('accounts/', include('accounts.urls')), #application accounts
    path('todolist/', include('todolist.urls')),  # Ajouter l'application todolist
]