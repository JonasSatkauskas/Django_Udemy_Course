from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.EmailField(max_length=100)

    def __str__(self):

        return self.first_name
