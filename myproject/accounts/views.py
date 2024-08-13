# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Vue pour l'inscription des utilisateurs
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Crée un nouvel utilisateur
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # Connecte l'utilisateur
            return redirect('home')  # Redirige vers la page d'accueil
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home(request):
     # Vérifiez si l'utilisateur est authentifié
    if request.user.is_authenticated:
        username = request.user.username  # Récupérez le nom d'utilisateur
    else:
        username = None  # Si l'utilisateur n'est pas connecté

    # Passez le nom d'utilisateur au template
    return render(request, 'home.html', {'username': username})