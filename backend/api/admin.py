from django.contrib import admin
from .models import Customer, Individual, Company, Bank, Brokerage, CryptoWallet, Government,Account, Transaction, AccountType

admin.site.register(Customer)
admin.site.register(Individual)
admin.site.register(Company)
admin.site.register(Bank)
admin.site.register(Brokerage)
admin.site.register(CryptoWallet)
admin.site.register(Government)

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(AccountType)
