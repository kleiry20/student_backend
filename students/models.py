from django.db import models

# Create your models here.
class Student(models.Model):
    studID = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.fname + " " + self.lname