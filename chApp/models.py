from django.db import models

# Create your models here.


class Test(models.Model):
    test_field = models.CharField(max_length=200)

    def __str__(self):
        return self.test_field
