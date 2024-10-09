from django.contrib import admin
from .models import Company , Expense , Account , Income

admin.site.register(Company)
admin.site.register(Account)
admin.site.register(Income)
admin.site.register(Expense)
