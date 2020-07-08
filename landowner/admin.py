from django.contrib import admin
from .models import Owner
from .models import Bill_Categories

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display =["name","contact","address","create"]
    list_display_links =["name"]
    search_fields=["name","contact","address"]
    list_editable=['contact']
    list_filter =["create","update"]

admin.site.register(Owner,OwnerAdmin),
admin.site.register(Bill_Categories)