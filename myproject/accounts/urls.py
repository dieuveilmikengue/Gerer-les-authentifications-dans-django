from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.contrib.auth.views import LogoutView
from accounts.views import profile

urlpatterns = [
    path('signup/', accounts_views.signup_view, name='signup'),  # URL d'inscription
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL de connexion
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Redirection après déconnexion
    path('', accounts_views.home, name='home'),  # URL de la page d'accueil
    
    # Password change views
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Profil
    path('profile/', accounts_views.profile, name='profile'),  # Profile
]