
import random

class Customer:
  def __init__(self, customer_number, name, email):
    self.customer_number = customer_number
    self.name = name
    self.email = email
    self.accounts = {}

  def add_account(self, account):
    self.accounts[account.account_number] = account

  def display(self):
    print(f"Customer Number: {self.customer_number}")
    print(f"Customer Name: {self.name}")
    print(f"Email: {self.email}")

class Account:
  def __init__(self, account_number):
    self.account_number = account_number

  def display(self):
    print(f"Account Number: {self.account_number}")

class CreditAccount(Account):
  def __init__(self, account_number, credit_limit):
    super().__init__(account_number)
    self.credit_limit = credit_limit

  def display(self):
    super().display()
    print(f"Credit Limit: {self.credit_limit}")

class DebitAccount(Account):
  def __init__(self, account_number, balance):
    super().__init__(account_number)
    self.balance = balance

  def display(self):
    super().display()
    print(f"Balance: {self.balance}")

class HybridAccount(CreditAccount, DebitAccount):
  def __init__(self, account_number, credit_limit, balance):
    CreditAccount.__init__(self, account_number, credit_limit)
    DebitAccount.__init__(self, account_number, balance)

  def display(self):
    CreditAccount.display(self)
    DebitAccount.display(self)

def create_credit_account(customer):
  print(f"Creating credit account for {customer.customer_number}")
  account_number = random.randint(1, 1000)
  account = CreditAccount(account_number, 100)
  customer.add_account(account)

def create_debit_account(customer):
  initial_deposit = int(input("Enter the initial deposit: "))
  while initial_deposit <= 0:
    initial_deposit = int(input("Invalid amount. Please enter deposit greater than 0:"))
  print(f"Creating debit account for {customer.account_number}")
  account_number = random.randint(1, 1000)
  da = DebitAccount(account_number, initial_deposit)
  customer.add_account(da)

def create_hybrid_account(customer):
  initial_deposit = input("Enter the initial deposit: ")
  while initial_deposit < 0:
    initial_deposit = input("Invalid amount. Please enter deposit 0 or greater than 0:")
  print(f"Creating hybrid account for {customer.customer_number}")
  account_number = random.randint(1, 1000)
  ha = HybridAccount(account_number, 100, initial_deposit)
  customer.add_account(ha)

def create_account():
  # Prompt the user to enter the option
  account_option = input('''Why type of Account you like to create?
  1. Credit Account
  2. Debit Account
  3. Hybrid Account
  ''')
  existing_customer = input("Are you existing customer (yes/no)?: ")
  if existing_customer == 'no':
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    customer_number = random.randint(1, 1000)
    customer = Customer(customer_number, name, email)
  else:
    customer_number = input("Enter your existing customer number: ")

  if account_option == '1':
    return create_credit_account(customer)
  elif account_option == '2':
    return create_debit_account(customer)
  elif account_option == '3':
    return create_hybrid_account(customer)
