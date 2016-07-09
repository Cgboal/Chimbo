from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=80)
    years = models.IntegerField()

    def __str__(self):
        return self.name

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Note(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

