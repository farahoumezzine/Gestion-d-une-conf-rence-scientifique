# UserApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil : quand l'utilisateur accède à l'URL racine (/)
    path('', views.home, name='home'),
    
    # Page d'inscription des nouveaux utilisateurs
    path('register/', views.register_user, name='register'),
    
    # Ajoutez d'autres chemins comme 'login' ou 'profile' ici plus tard
]