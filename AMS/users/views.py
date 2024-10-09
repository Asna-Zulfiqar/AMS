from django.shortcuts import render , redirect , HttpResponse , get_object_or_404 
from .forms import RegistrationForm , CompanyUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth.decorators import login_required
from company.models import Company
from .models import CompanyUser


def home(request):
    return render(request, 'index.html')

def sign_in(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.save()
                return redirect('users:log_in')
    
    else:
        form = RegistrationForm()

    return render(request, 'signin.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"Authenticated user: {user.username}")
                if user.is_superuser:
                    auth_login(request, user)
                    return redirect('company:super_admin_report')
                elif user.is_staff:
                    auth_login(request, user)
                    return redirect('company:company_owner_view')
                elif user.is_active and not user.is_staff:
                    auth_login(request , user)
                    companyuser = CompanyUser.objects.get(user=user)
                    return redirect('users:company_user_view', user_id=companyuser.id)
                else:
                    return HttpResponse('Access Denied')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def add_user(request ):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        company_user_form = CompanyUserForm(request.POST)
        if user_form.is_valid() and company_user_form.is_valid():
            user = user_form.save()
            company_user = company_user_form.save(commit=False)
            company_user.user = user
            company_user.save()
            return redirect('company:company_owner_view')    
    if request.method == 'GET':
        user_form = RegistrationForm()
        company_user_form = CompanyUserForm()
    return render(request, 'add_user.html', {'user_form': user_form, 'company_user_form': company_user_form})

@login_required
def admin_report(request):
    companies = Company.objects.filter(owner=request.user) 
    company_users = []
    accounts = []
    incomes = []
    expenses = []
    

    for company in companies:
        company_users.extend(company.company_users.all())  
        accounts.extend(company.accounts.all())  
        incomes.extend(company.incomes.all())  
        expenses.extend(company.expenses.all())


    context = {
        'company_users': company_users, 
        'companies': companies,
        'accounts': accounts,
        'incomes': incomes, 
        'expenses': expenses
    }
    
    return render(request, 'admin_report.html', context)

@login_required
def company_user_view(request, user_id):
    company_user = get_object_or_404(CompanyUser, id=user_id)
    company = company_user.company
    return render(request, 'company_user_view.html', {'company_user': company_user, 'company': company})

@login_required
def user_report(request, companyuser_id):
    company_user = get_object_or_404(CompanyUser, id=companyuser_id)
    
    if company_user.report_perm:
        company = company_user.company
        accounts = company.accounts.all() 
        incomes = company.incomes.all()    
        expenses = company.expenses.all()  

        context = {
            'company_user': company_user,
            'company': company,
            'accounts': accounts,
            'incomes': incomes,
            'expenses': expenses,
        }
        return render(request, 'user_report.html', context)
    else:
        return HttpResponse('Access Denied: Insufficient Permissions')