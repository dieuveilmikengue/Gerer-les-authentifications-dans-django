# todolist/models.py

from django.db import models
from django.conf import settings  # Pour accéder à AUTH_USER_MODEL

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Lien vers le modèle utilisateur
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
