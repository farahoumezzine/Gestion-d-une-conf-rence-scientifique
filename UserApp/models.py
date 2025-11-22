from django.db import models
import uuid

# --- Classe de Base (Réutilisée) ---
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Dernière Modification")

    class Meta:
        abstract = True
        ordering = ['-created_at'] 
# --- Fin Classe de Base ---


class AbstractUser(BaseModel):
    """Héritage pour le modèle User."""
    # Aucun champ spécifique ici, sert de point d'héritage.
    class Meta:
        abstract = True


class User(AbstractUser):
    # --- Choix pour l'attribut 'role' ---
    ROLE_CHOICES = [
        ('participant', 'Participant'),
        ('organisateur', 'Organisateur'),
        ('comite_scientifique', 'Membre du Comité Scientifique'),
    ]
    
    # Nouvelle clé primaire de longueur 8 (Char/UUID pour une longueur fixe)
    # Nous utilisons CharField pour une longueur fixe, car UUIDField génère 32 caractères.
    user_id = models.CharField(
        max_length=8, 
        primary_key=True, 
        editable=False, 
        unique=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    
    # 'role' avec les contraintes de choix
    role = models.CharField(
        max_length=50, 
        choices=ROLE_CHOICES, 
        default='participant' # Rôle par défaut si l'utilisateur s'inscrit lui-même
    )
    nationality = models.CharField(max_length=100, blank=True, null=True)
    
    # 'email' comme EmailField et unique
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        # Générer l'ID de 8 caractères lors de la première sauvegarde
        if not self.user_id:
            self.user_id = str(uuid.uuid4()).replace('-', '')[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"