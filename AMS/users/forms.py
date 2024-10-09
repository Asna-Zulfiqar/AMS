from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CompanyUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']


class CompanyUserForm(forms.ModelForm):

    class Meta:
        model = CompanyUser
        fields = ['company', 'report_perm']