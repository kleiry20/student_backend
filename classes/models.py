from django.db import models

# Create your models here.
class Standard(models.Model):
    stdID = models.CharField(max_length=200)
    stdName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.stdName 