import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django

django.setup()

### FAKE USERS SCRIPT ###

import random
from AppTwo.models import User
from faker import Faker

fake = Faker()


def populate(N=5):

    for entry in range(N):

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()


        usr = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('Populating complete!')


