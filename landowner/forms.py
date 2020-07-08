from django import forms
from .models import Owner
from .models import Bill_Categories
from .models import Bill_table

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name','email','contact','address']

class Bill_CategoriesForm(forms.ModelForm):
    class Meta:
        model = Bill_Categories
        fields = ['name','color','icon']

class Bill_tableForm(forms.ModelForm):
    class Meta:
        model = Bill_table
        fields = ['landowner_id','bill_category_id','bill_category_name','bill_amount','form_date','to_date','payment_date','receipt_image','note',]