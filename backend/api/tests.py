from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Individual, Account, AccountType, Transaction

class CustomerAccountTests(TestCase):
    def setUp(self):
        # Create a user for testing Individual linked to User
        self.user = User.objects.create_user(username='john_doe', password='12345')
        
        # Create an Individual Customer
        self.individual = Individual.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            location='1234 Test St',
            contact_email='john@example.com',
            phone_number='1234567890'
        )
        
        # Create an AccountType
        self.account_type = AccountType.objects.create(
            type_name='Checking',
            description='A standard checking account'
        )
        
        # Create an Account
        self.account = Account.objects.create(
            customer=self.individual,
            account_name='John Checking Account',
            account_number='0123456789',
            account_type=self.account_type,
            currency='USD',
            balance=100.00  # starting with a balance
        )

    def test_account_creation(self):
        # Test that the account was created and is linked to the right customer
        self.assertEqual(self.account.customer, self.individual)
        self.assertEqual(self.account.balance, 100.00)
        self.assertEqual(self.account.currency, 'USD')

    def test_transaction(self):
        # Create another account for transaction testing
        self.account2 = Account.objects.create(
            customer=self.individual,
            account_name='John Savings Account',
            account_number='9876543210',
            account_type=self.account_type,
            currency='USD',
            balance=200.00
        )
        
        # Create a transaction
        self.transaction = Transaction.objects.create(
            from_account=self.account,
            to_account=self.account2,
            amount=50.00,
            description='Transfer to savings'
        )
        
        # Test that balances are updated correctly
        self.account.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account.balance, 50.00)
        self.assertEqual(self.account2.balance, 250.00)
        self.assertEqual(self.transaction.amount, 50.00)
        self.assertEqual(self.transaction.from_account, self.account)
        self.assertEqual(self.transaction.to_account, self.account2)

    def test_customer_str(self):
        # Test the string representation of the customer
        self.assertEqual(str(self.individual), 'John Doe')

    def test_account_str(self):
        # Test the string representation of the account
        self.assertEqual(str(self.account), 'John Checking Account - 0123456789')
        
