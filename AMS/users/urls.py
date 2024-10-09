from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('accounts/login/', views.log_in, name='log_in'),
    path('add_user/', views.add_user, name='add_user'),
    path('admin_report/', views.admin_report, name='admin_report'),
    path('company_user<int:user_id>/' , views.company_user_view , name = 'company_user_view'),
    path('user_report<int:companyuser_id>/' , views.user_report , name='user_report')
]
