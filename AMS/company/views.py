from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Company , Account , Income , Expense
from .forms import AddCompany , AccountForm , IncomeForm , ExpenseForm
from users.models import CompanyUser

@login_required
def company_owner_view(request):
    companies = Company.objects.filter(owner = request.user) 
    return render(request , 'company_owner_view.html' , {'companies' : companies })

@login_required
def add_company(request):
    if request.method == 'POST':
        form = AddCompany(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect('company:company_owner_view')
    if request.method == 'GET':
        form = AddCompany()
        return render(request , 'add_company.html' , {'form':form})
    
@login_required
def company_detail(request , company_id):
    company = get_object_or_404(Company , id = company_id)
    users = company.company_users.all()
    accounts = company.accounts.all()
    incomes = company.incomes.all()
    expenses = company.expenses.all()
    context = {'company':company ,
               'users':users,
               'accounts':accounts ,
               'incomes':incomes ,
               'expenses':expenses}
    return render(request , 'company_detail.html' , context )

@login_required
def add_account(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.company = company
            account.save()
            return redirect('company:company_detail', company_id=company.id)
    if request.method == 'GET':
        form = AccountForm()
        return render(request, 'add_account.html', { 'form': form ,'company': company})
    

@login_required
def add_income(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.company = company
            income.save()
            return redirect('company:company_detail', company_id=company.id)
    if request.method == 'GET':
        form = IncomeForm()
        return render(request, 'add_income.html', { 'form': form ,'company': company})
    

@login_required
def submit_expense(request, companyuser_id):
    company_user = get_object_or_404(CompanyUser , id = companyuser_id)
    company = company_user.company
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.company = company 
            expense.added_by = company_user
            expense.save()
            return HttpResponse('Expense Added')

    if request.method == 'GET':
        form = ExpenseForm()
        return render(request, 'submit_expense.html', {'form': form, 'company': company})


@login_required    
def super_admin_report(request):
    companies = Company.objects.all()
    company_users = CompanyUser.objects.all()
    accounts = Account.objects.all()
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    context = {
        'companies': companies,
        'accounts': accounts,
        'incomes': incomes,
        'expenses': expenses,
        'company_users': company_users
    }
    
    return render(request, 'super_admin_report.html', context)
         
        