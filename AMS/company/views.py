from django.shortcuts import render, redirect , get_object_or_404, HttpResponse
from .models import Company, Accounts , Income , Expense , CompanyUsers
from .forms import RegistrationForm , AccountForm , IncomeForm , AddCompany , CompanyUserForm , CustomUserForm , ExpenseForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request , 'index.html')

def super_admin_view(request):
    companies = Company.objects.all()
    accounts = Accounts.objects.all()
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    context = {
        'companies': companies,
        'accounts': accounts,
        'incomes': incomes,
        'expenses': expenses,
    }
    return render(request, 'super_admin_view.html', context)

def sign_in(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.save()
                return redirect('login_view')
    
    else:
        form = RegistrationForm()

    return render(request, 'sigin.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    auth_login(request, user)
                    return redirect('super_admin_view')
                elif user.is_staff:
                    auth_login(request, user)
                    return redirect('owner')
                else:
                    return HttpResponse('Access Denied')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


 
def owner(request):
    companies = Company.objects.filter(owner = request.user)
    
    return render(request , 'owner.html' , {'companies' : companies })


def company_detail(request , company_id):
    company = get_object_or_404(Company , id = company_id)
    users = company.company_users.all()
    return render(request , 'detail.html' ,  {'company' : company , 'users' : users })


@login_required
def add_company(request):
    if request.method == 'POST':
        form = AddCompany(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner')
    else:
        form = AddCompany()
        return render(request , 'add_company.html' , {'form':form}) 
       
@login_required
def create_account(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.company = company
            account.save()
            return redirect('company_detail', company_id=company.id)
    else:
        form = AccountForm()
    return render(request, 'create_account.html', { 'form': form ,'company': company})


@login_required
def add_income(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.company = company
            income.save()
            return redirect('company_detail', company_id=company.id)
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', { 'form': form ,'company': company})

def accounts(request , company_id):
    company = get_object_or_404(Company , id=company_id)
    accounts = company.accounts.all()
    return render(request , 'account.html' , {'accounts': accounts})

def income(request , company_id):
    company = get_object_or_404(Company , id = company_id)
    income = company.incomes.all()
    return render(request , 'income.html' , {'income':income})

def company_user(request ):
    if request.method == 'POST':
        form = CompanyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner')    
    else:
        form = CompanyUserForm()
        return render(request , 'add_user.html', {'form':form} )    
    
def check_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = CompanyUsers.objects.get(username=username , password = password)
            if user:
                return redirect('company_user_view' , user_id = user.id )
            else:
                return HttpResponse('Access Denied due to Invalid Crendtials...')
    if request.method == 'GET':
        form = CustomUserForm()
        return render(request , 'company_user_login.html' , {'form':form})

def company_user_view(request, user_id):
    company_user = get_object_or_404(CompanyUsers, id=user_id)
    company = company_user.relation_to 
    return render(request, 'company_user_view.html', {'company_user': company_user,'company': company})
       
def submit_expense(request, company_id):
    company = get_object_or_404(Company, id=company_id)


    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.company = company 
            expense.save()
            return HttpResponse('Expense Added')
    else:
        form = ExpenseForm()

    return render(request, 'submit_expense.html', {'form': form, 'company': company})

def report_request(request , user_id):
    company_user = get_object_or_404(CompanyUsers, id=user_id)
    if company_user.report_perm:
        company = company_user.relation_to
        accounts = company.accounts.all()
        incomes = company.incomes.all()
        expenses = company.expenses.all()
        context = {'company_user': company_user, 
                   'company': company,
                    'accounts': accounts,
                    'incomes': incomes, 
                    'expenses': expenses
                    }
        return render(request, 'report.html', context)
    else:
        return HttpResponse('Access Denied due to Insufficient Permissions...')
    
def admin_report(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company_users = CompanyUsers.objects.filter(relation_to=company)
    accounts = company.accounts.all()
    incomes = company.incomes.all()
    expenses = company.expenses.all()
    
    context = {
        'company_user': company_users, 
        'company': company,
        'accounts': accounts,
        'incomes': incomes, 
        'expenses': expenses
    }
    
    return render(request, 'admin_report.html', context)




