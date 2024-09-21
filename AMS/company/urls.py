from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('super_admin_view' , views.super_admin_view , name = 'super_admin_view'),
    path('company_user_view<int:user_id>/' , views.company_user_view , name = 'company_user_view'),
    path('signin/' , views.sign_in , name = 'sign_in'),
    path('login/' , views.login_view , name='login_view'),
    path('owner/' , views.owner , name = 'owner'),
    path('add_company/' , views.add_company , name = 'add_company'),
    path('detail<int:company_id>/' , views.company_detail , name = 'company_detail'),
    path('create_account<int:company_id>/' , views.create_account , name = 'create_account'),
    path('add_income<int:company_id>/' , views.add_income , name = 'add_income'),
    path('accounts<int:company_id>/' , views.accounts , name='accounts'),
    path('income<int:company_id>/' , views.income , name='income'),
    path('add_user/' , views.company_user , name = 'add_user'),
    path('check_user/' , views.check_user , name='check_user'),
    path('add_expense<int:company_id>/' , views.submit_expense , name ='submit_expense'),
    path('report<int:user_id>/' , views.report_request , name='report_request'),
    path('admin_report<int:company_id>/' , views.admin_report , name = 'admin_report'),

]