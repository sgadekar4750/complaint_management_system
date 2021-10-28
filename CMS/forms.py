from django import forms
from django.contrib.auth.models import User
from CMS.models import *

from django.forms import ModelForm



class UserForm(forms.ModelForm):
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput())
    class Meta:
       	model = User
        fields = ['username','email','password']


class InfoProfileForm(forms.ModelForm):
	class Meta:
		model = Profiles
		fields = ['first_name','last_name','gender','tax_id_number','age','address','area','pin','mobile']


class ComplaintForm(forms.ModelForm):
	class Meta:
		model = Complaint
		fields = ['sub_muncipal_division','area','complaint_desc','address','type_of_complaint','user']
    
class OrderForm(forms.ModelForm):
	class Meta:
		model = Complaint
		fields = ['solved']

class StatusForm(forms.Form):
    idnumber = forms.CharField()


   

   