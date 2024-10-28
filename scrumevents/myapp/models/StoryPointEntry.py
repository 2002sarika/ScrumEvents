# myapp/models.py
from django.db import models

class StoryPointEntry(models.Model):
    username = models.CharField(max_length=100)
    story_points = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.username}: {self.story_points} points"
