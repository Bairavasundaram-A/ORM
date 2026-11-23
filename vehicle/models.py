from django.db import models
from django.contrib import admin

class Vehicle_DB(models.Model):
    vehicle_No=models.CharField(max_length=10)
    coustomer_Name=models.CharField(max_length=10)
    vehicle_model=models.CharField(max_length=20)
    Email=models.EmailField()
    phone_No=models.IntegerField()
    Address=models.TextField()
    cost=models.FloatField()

class Vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["vehicle_No","coustomer_Name","vehicle_model","Email","phone_No","Address","cost"]