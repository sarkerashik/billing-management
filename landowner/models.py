from django.db import models

# Create your models here.

class Owner(models.Model):

    user_id = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    address = models.TextField()
    create = models.DateTimeField(auto_now=False,auto_now_add=True)
    update = models.DateTimeField(auto_now=True,auto_now_add=False)