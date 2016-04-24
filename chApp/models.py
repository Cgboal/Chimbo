from django.db import models

# Create your models here.


class Test(models.Model):
    test_field = models.CharField(max_length=200)

    def __str__(self):
        return self.test_field


class User(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)