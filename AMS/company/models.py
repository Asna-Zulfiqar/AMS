from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_companies')

    def __str__(self):
        return self.company_name
    
class Accounts(models.Model):
    company= models.ForeignKey(Company , on_delete=models.CASCADE , related_name='accounts')
    account_name = models.CharField(max_length=200)
    balance = models.IntegerField()

    def __str__(self):
        return self.account_name

class Income(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='company')
    income = models.IntegerField()

    def __str__(self):
        return f"{self.company} has {self.income} income"

class Expense(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='expenses')
    amount = models.IntegerField()
    added_by = models.ForeignKey(User , on_delete=models.CASCADE )
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.amount}'

class Report(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='reports')
    data = models.TextField()
    generated_on = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Report generated on {self.generated_on}'


class CompanyUsers(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    username = models.CharField(max_length=100)
    password = models.IntegerField()
    relation_to = models.ForeignKey(Company , on_delete=models.CASCADE , related_name='company_users')