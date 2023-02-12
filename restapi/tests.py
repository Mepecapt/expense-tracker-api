from django.test import TestCase
from restapi import models

# Create your tests here.

class TestModel(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(amount=249.99, merchant='Amazon', description="anc headphones", category='music')
        inserter_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserter_expense.amount)
        self.assertEqual('Amazon', inserter_expense.merchant)
        self.assertEqual("anc headphones", inserter_expense.description)
        self.assertEqual('music', inserter_expense.category)