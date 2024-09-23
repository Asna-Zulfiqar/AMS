from django.contrib import admin
from .models import Accounts , Company , Expense , Income , CompanyUsers

admin.site.register(Company)
admin.site.register(Accounts)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(CompanyUsers)
