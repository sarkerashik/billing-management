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



class Bill_Categories(models.Model): 
    user_id = models.IntegerField()
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    icon = models.ImageField(upload_to="pic")
    create = models.DateTimeField(auto_now=False,auto_now_add=True)
    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        db_table = 'bill_categories'


class Bill_table(models.Model):
    created_by = models.IntegerField()
    landowner_id = models.IntegerField()
    bill_category_id = models.IntegerField()
    bill_category_name = models.CharField(max_length=255)
    bill_amount = models.FloatField()
    form_date = models.IntegerField()
    to_date = models.IntegerField()
    payment_date = models.IntegerField()
    receipt_image = models.ImageField(upload_to='bill')
    note = models.CharField(max_length=500)
    class Meta:
        db_table = 'bills'