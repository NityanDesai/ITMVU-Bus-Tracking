from django.db import models
from django.contrib.auth.models import AbstractUser

class Bus(models.Model):
    bus_route_no = models.IntegerField(primary_key = True)
    role_id = models.IntegerField(blank=True, default='1')
    driver_name = models.CharField(max_length=100)
    driver_mobile_no = models.BigIntegerField()
    username = models.CharField(max_length=103)
    password = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.bus_route_no)

class User(AbstractUser):
    id = models.AutoField(primary_key=True) 
    roll_no = models.CharField(max_length=30, null=True)
    bus_route_no = models.ForeignKey(Bus, null=True, on_delete=models.SET_NULL)
    parent_name = models.CharField(max_length=100, null=True)
    parent_mobile_no = models.BigIntegerField(null=True)
    parent_email = models.EmailField(max_length=100, null=True)

class driver(models.Model):
    bus_route_no = models.IntegerField(primary_key= True)
    role_id = models.IntegerField(blank=True, default='0')
    driver_mobile_no=models.BigIntegerField()
    driver_name=models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)