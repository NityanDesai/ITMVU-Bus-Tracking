from django import forms
from django.forms import ModelForm
from bus.models import Bus, User, driver


class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_route_no','driver_name','driver_mobile_no', 'username', 'password'] #,'username'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name', 'last_name', 'email', 'roll_no', 'bus_route_no', 'parent_name', 'parent_mobile_no', 'parent_email']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'roll_no', 'bus_route_no', 'parent_name', 'parent_mobile_no', 'parent_email']


class driverForm(ModelForm):
    class Meta:
        model = driver
        fields = ['username','password']
        #fields = ['username','password','bus_route_no']



class driverUpdateForm(ModelForm):
    class Meta:
        model = driver
        fields = ['driver_name','bus_route_no','driver_mobile_no']