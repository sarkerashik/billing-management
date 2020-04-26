from django.db import models

# Create your models here.

class Owner(models.Model):

    serial = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.TextField()
