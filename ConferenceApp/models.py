from django.db import models
from UserApp.models import BaseModel, User # Import de la base et du modèle User

# --- Modèle Conference ---
class Conference(BaseModel):
    # --- Choix pour l'attribut 'theme' ---
    THEME_CHOICES = [
        ('CS_AI', 'Computer Science & Artificial Intelligence'),
        ('SE', 'Science & Engineering'),
        ('SS_EDU', 'Social Sciences & Education'),
        ('INTER', 'Interdisciplinary Themes'),
    ]
    
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    # 'theme' avec les contraintes de choix
    theme = models.CharField(
        max_length=50, 
        choices=THEME_CHOICES, 
        blank=True, 
        null=True
    )
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # 'description' comme TextField
    description = models.TextField(blank=True, null=True)
    
    organizers = models.ManyToManyField(
        User, 
        through='OrganizingCommittee', 
        related_name='conferences_organized'
    )

    def __str__(self):
        return self.name

# --- Modèle OrganizingCommittee ---
class OrganizingCommittee(BaseModel):
    # --- Choix pour l'attribut 'committee_role' ---
    COMMITTEE_ROLE_CHOICES = [
        ('chair', 'Chair'),
        ('co_chair', 'Co-Chair'),
        ('member', 'Member'),
        ('review_coord', 'Review Coordinator'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    
    # 'committee_role' avec les contraintes de choix
    committee_role = models.CharField(
        max_length=50, 
        choices=COMMITTEE_ROLE_CHOICES
    )
    # 'date_joined' comme DateField
    date_joined = models.DateField() 

    class Meta:
        unique_together = ('user', 'conference')

    def __str__(self):
        return f"{self.user.last_name} - {self.committee_role} ({self.conference.name})"


# --- Modèle Submission ---
class Submission(BaseModel):
    # --- Choix pour l'attribut 'status' ---
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    submission_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    
    # 'abstract' comme TextField
    abstract = models.TextField()
    
    topic = models.CharField(max_length=255)
    
    # 'keywords' comme CharField (séparés par des virgules)
    keywords = models.CharField(max_length=500)
    
    # 'paper' comme FileField
    paper_file = models.FileField(upload_to='papers/', blank=True, null=True, verbose_name='Article Soumis')
    
    # 'status' avec les contraintes de choix
    status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES, 
        default='submitted'
    ) 
    
    # 'submission_date' comme DateField avec auto_now_add=True
    submission_date = models.DateField(auto_now_add=True) 
    
    # 'payed' comme BooleanField
    payed = models.BooleanField(default=False)
    
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='submissions_authored'
    )
    conference = models.ForeignKey(
        Conference, 
        on_delete=models.CASCADE, 
        related_name='submissions'
    ) 

    def __str__(self):
        return self.title