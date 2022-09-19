from email.policy import default
from django.db import models
from classes.models import Standard
from students.models import Student

# Create your models here.

class StudentClassMap(models.Model):
    stdID = models.ForeignKey(Standard, on_delete=models.CASCADE)
    studID = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.FloatField(default=0.0)
    rank = models.IntegerField(default=0)

    
    def __str__(self):
        return str(self.studID)
