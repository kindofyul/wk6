from django.db import models
from django import forms

class Community(models.Model):
    title = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    # now = models.BooleanField(default=False)
    review = models.TextField()

    # def __str__(self):
    #     return self.title