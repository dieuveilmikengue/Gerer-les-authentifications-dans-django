# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Vue pour l'inscription des utilisateurs
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home(request):
     # Vérifiez si l'utilisateur est authentifié
    if request.user.is_authenticated:
        username = request.user.username  # Récupérez le nom d'utilisateur
    else:
        username = None  # Si l'utilisateur n'est pas connecté

    # Passez le nom d'utilisateur au template
    return render(request, 'home.html', {'username': username})

@login_required
def profile(request):
    """Affiche les informations du profil de l'utilisateur."""
    user = request.user  # Récupère l'utilisateur connecté
    return render(request, 'accounts/profile.html', {'user': user})