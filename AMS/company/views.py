from django.shortcuts import render, redirect , get_object_or_404, HttpResponse
from .models import Company, Accounts , Income , Expense
from .forms import RegistrationForm , AccountForm , IncomeForm , AddCompany , CompanyUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request , 'index.html')


def sign_in(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
                form.save()
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
                if user.is_staff:
                    auth_login(request, user)
                    return redirect('owner')
                elif user.is_superuser:
                    auth_login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Access Denied')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

 
def owner(request):
    companies = Company.objects.filter(owner = request.user)
    return render(request , 'owner.html' , {'companies' : companies})


def company_detail(request , company_id):
    company = get_object_or_404(Company , id = company_id)
    return render(request , 'detail.html' ,  {'company' : company })


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
            form.save()
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
            form.save()
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
    income = company.company.all()
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