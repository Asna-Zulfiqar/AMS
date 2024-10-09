from django.db import models
from django.contrib.auth.models import User
from users.models import CompanyUser

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_companies')

    def __str__(self):
        return self.company_name
    
class Account(models.Model):
    company= models.ForeignKey(Company , on_delete=models.CASCADE , related_name='accounts')
    account_name = models.CharField(max_length=200)
    balance = models.IntegerField()

    def __str__(self):
        return self.account_name

class Income(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='incomes')
    income = models.IntegerField()

    def __str__(self):
        return f"{self.income}"


class Expense(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='expenses')
    amount = models.IntegerField()
    added_by = models.ForeignKey(CompanyUser , on_delete=models.CASCADE )
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.amount}'    
    



