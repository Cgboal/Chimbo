from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=20)
    pHash = models.CharField(max_length=32)
    perms = models.PositiveSmallIntegerField()
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    country = CountryField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.userName
