# expenses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
import datetime

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('expense_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def expense_list(request):
    # Get selected month from session or default to current month
    today = datetime.date.today()
    selected_month = request.session.get('selected_month')
    
    if selected_month:
        try:
            year, month = map(int, selected_month.split('-'))
        except (ValueError, AttributeError):
            year, month = today.year, today.month
    else:
        year, month = today.year, today.month
    
    # Handle month filter form submission
    if request.method == 'POST' and 'month_filter' in request.POST:
        selected_month = request.POST.get('month_filter')
        request.session['selected_month'] = selected_month
        if selected_month:
            year, month = map(int, selected_month.split('-'))
    
    # Filter expenses by user and selected month
    expenses = Expense.objects.filter(user=request.user)
    
    if selected_month:
        expenses = expenses.filter(date__year=year, date__month=month)
    
    expenses = expenses.order_by('-date')
    
    # Calculate totals
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0.00
    
    # Calculate period totals
    last_7_days = today - datetime.timedelta(days=7)
    last_30_days = today - datetime.timedelta(days=30)
    
    user_expenses = Expense.objects.filter(user=request.user)
    weekly_total = user_expenses.filter(date__gte=last_7_days).aggregate(Sum('amount'))['amount__sum'] or 0.00
    monthly_total = user_expenses.filter(date__gte=last_30_days).aggregate(Sum('amount'))['amount__sum'] or 0.00
    all_time_total = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0.00
    
    # Generate month options for the filter
    month_options = []
    for i in range(12):  # Last 12 months
        date = today.replace(day=1) - datetime.timedelta(days=i * 30)
        month_options.append({
            'value': f"{date.year}-{date.month:02d}",
            'label': date.strftime('%B %Y')
        })
    
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'weekly_total': weekly_total,
        'monthly_total': monthly_total,
        'all_time_total': all_time_total,
        'selected_month': selected_month or f"{year}-{month:02d}",
        'month_options': month_options,
        'current_month_name': datetime.date(year, month, 1).strftime('%B %Y'),
    }
    return render(request, 'expenses/expense_list.html', context)

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form, 'expense': expense})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})