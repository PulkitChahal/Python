from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=200)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=200)

    def __str__(self):
        return str(self.eno)