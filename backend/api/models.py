from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AccountType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type_name
class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=255)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, related_name='accounts')
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    is_owned = models.BooleanField(default=True)
    
    def __str__(self):
        return self.customer + ' ' + self.account_number

from django.db import models

class Transaction(models.Model):
    from_account = models.ForeignKey(
        'Account', 
        related_name='transactions_out', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    to_account = models.ForeignKey(
        'Account', 
        related_name='transactions_in', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.from_account} to {self.to_account} - {self.amount}"


