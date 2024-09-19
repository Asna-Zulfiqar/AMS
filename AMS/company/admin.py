from django.contrib import admin
from .models import Accounts , Company , Report , Expense , Income , CompanyUsers

admin.site.register(Company)
admin.site.register(Report)
admin.site.register(Accounts)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(CompanyUsers)
