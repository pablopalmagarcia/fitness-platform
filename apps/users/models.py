from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Extended profile for users.
    Each profile belongs to one user and stores their liked exercises, routines, and meals.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exercises_liked = models.JSONField(default=list)
    routines_liked = models.JSONField(default=list)
    meals_liked = models.JSONField(default=list)
    def __str__(self):
        return self.user.username