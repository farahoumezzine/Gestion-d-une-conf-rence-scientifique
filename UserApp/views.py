# UserApp/views.py (Mise à jour)

from django.shortcuts import render, redirect
# Note: Nous n'avons plus besoin de HttpResponse ici

def home(request):
    # Remplacer HttpResponse par un rendu de template
    return render(request, 'UserApp/home.html')

def register_user(request):
    if request.method == 'POST':
        # La logique de traitement du formulaire viendra ici
        return redirect('home') # Rediriger l'utilisateur après inscription réussie
    else:
        # Rendre le template du formulaire
        return render(request, 'UserApp/register.html')