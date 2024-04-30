from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return f"self.title"
    

# Base Customer model
class Customer(models.Model):
    #customer_type = models.CharField(max_length=50)  # could be individual, company, etc.
    location = models.CharField(max_length=255, null=True, blank=True)  # Assuming a single string can represent the location
    contact_email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
class Individual(Customer):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Company(Customer):
    name = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Bank(Customer):
    name = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Brokerage(Customer):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class CryptoWallet(Customer):
    name = models.CharField(max_length=255)
    supported_currencies = models.CharField(max_length=255, null=True, blank=True)
    wallet_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Government(Customer):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class AccountType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type_name}"
    

class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    account_name = models.CharField(max_length=255, unique=True)
    account_number = models.CharField(max_length=255)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, related_name='accounts')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Default balance set to 0
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.account_name} - {self.account_number}"


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


