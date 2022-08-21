from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
