from django.db import models
from UserApp.models import BaseModel
from ConferenceApp.models import Conference, Submission # Import des modèles nécessaires

class Session(BaseModel):
    session_id = models.AutoField(primary_key=True)
    
    # 'title' comme CharField
    title = models.CharField(max_length=255)
    
    # 'topic' comme CharField
    topic = models.CharField(max_length=255)
    
    # 'session_day' comme DateField
    session_day = models.DateField()
    
    # 'start_time' et 'end_time' comme TimeField
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    # 'room' comme CharField
    room = models.CharField(max_length=100)
    
    # Relation Many-to-One avec Conference
    conference = models.ForeignKey(
        Conference, 
        on_delete=models.CASCADE, 
        related_name='sessions'
    )
    
    # Relation Many-to-Many avec Submission
    submissions = models.ManyToManyField(
        Submission, 
        related_name='sessions'
    ) 

    def __str__(self):
        return f"{self.title} ({self.conference.name})"