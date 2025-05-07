from django.db import models


# Create your models here.
class HyderabadJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()


class BangloreJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()


class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()


class NoidaJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
