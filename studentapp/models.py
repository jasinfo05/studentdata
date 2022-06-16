from datetime import date
from django.db import models

class candidate(models.Model):
    Name=models.CharField(max_length=50)
    DOB=models.DateField(default=date)
    Class=models.CharField(max_length=10)
    Division=models.CharField(max_length=10)
    Gender=models.CharField(max_length=20)
    Admission_No=models.CharField(max_length=10)

    def __str__(self):
        return self.Name
