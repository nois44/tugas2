from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.CharField(max_length=255)