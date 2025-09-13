# expenses/models.py
from django.db import models
from django.utils import timezone

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title