from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Accounts , Income , Company , CompanyUsers

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['owner','company_name']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['company','account_name','balance']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['company' , 'income']

class CompanyUserForm(forms.ModelForm):
    class Meta:
        model = CompanyUsers
        fields = ['first_name' , 'last_name' , 'relation_to' , 'username' , 'password']