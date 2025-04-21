from django.db import models


# Create your models here.
class Employees(models.Model):
    empid = models.IntegerField()
    ename = models.CharField(max_length=20)
    eaddress = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.ename

    class Meta:
        db_table = 'employee'


class Manager(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    age = models.IntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    age = models.IntegerField()