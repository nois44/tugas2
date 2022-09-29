from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    