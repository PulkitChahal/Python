import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd079_crudProject.settings')
import django

django.setup()

from testApp.models import *
from faker import Faker
from random import *

faker = Faker()


def populate(n):
    for i in range(n):
        feno = randint(1001, 99999)
        fename = faker.name()
        fesal = randint(100000, 200000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)


populate(20)
