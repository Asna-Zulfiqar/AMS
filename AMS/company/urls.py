from django.urls import path
from . import views

urlpatterns = [
    path('' , views.company_owner_view , name='company_owner_view'),
    path('add_company/' , views.add_company , name = 'add_company'),
    path('details<int:company_id>/' , views.company_detail , name ='company_detail'),
    path('add_account<int:company_id>/' , views.add_account , name = 'add_account'),
    path('add_income<int:company_id>/' , views.add_income , name = 'add_income'),
    path('add_expense/<int:companyuser_id>/' , views.submit_expense , name='submit_expense'),
    path('super_admin/' , views.super_admin_report , name = 'super_admin_report')
]