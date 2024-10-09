from django import forms
from .models import Company , Account , Income , Expense

class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name','balance']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount' ]        