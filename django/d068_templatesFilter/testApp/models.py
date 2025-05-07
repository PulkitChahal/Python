from django.db import models

# Create your models here.
class FilterModel(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    date = models.DateField()
