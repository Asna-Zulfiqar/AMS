from django.db import models
from django.contrib.auth.models import User

class CompanyUser(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE )  
    report_perm = models.BooleanField(default=False) 
    company = models.ForeignKey('company.Company' , on_delete=models.CASCADE , related_name='company_users')

    def __str__(self):
        return f"{self.user.username}"