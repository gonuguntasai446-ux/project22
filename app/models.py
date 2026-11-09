
from django.db import models

class Employee(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    ROLE = models.CharField(max_length=100)
    SALARY = models.DecimalField(max_digits=10, decimal_places=2)
    DATE_OF_JOIN = models.DateField()
    BONUS = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.NAME
