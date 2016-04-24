from django.db import models

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=20)
    pHash = models.CharField(max_length=32)
    perms = models.PositiveSmallIntegerField()
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.userName
