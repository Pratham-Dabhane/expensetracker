# expenses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
import datetime

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0.00
    
    # Calculate totals for charts (optional but cool)
    today = datetime.date.today()
    last_7_days = today - datetime.timedelta(days=7)
    last_30_days = today - datetime.timedelta(days=30)
    
    weekly_total = Expense.objects.filter(date__gte=last_7_days).aggregate(Sum('amount'))['amount__sum'] or 0.00
    monthly_total = Expense.objects.filter(date__gte=last_30_days).aggregate(Sum('amount'))['amount__sum'] or 0.00
    
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'weekly_total': weekly_total,
        'monthly_total': monthly_total,
    }
    return render(request, 'expenses/expense_list.html', context)

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form, 'expense': expense})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})