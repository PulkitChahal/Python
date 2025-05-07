import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd060_jobPortal.settings')
import django

django.setup()

from testApp.models import *
from faker import Faker
from random import *

fake = Faker()


def phone_number_gen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Lead', 'Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphone_number = phone_number_gen()
        jobs_record = HyderabadJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                             eligibility=feligibility, address=faddress, email=femail,
                                                             phone_number=fphone_number)
        print(jobs_record)


populate(25)
