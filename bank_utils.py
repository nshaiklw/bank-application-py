
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
    for account in self.accounts.values():
      account.display()
      print()

class Account:
  def __init__(self, account_type, account_number, balance):
    self.account_number = account_number
    self.balance = balance
    self.account_type = account_type

  def credit(self, amount):
    self.balance += amount

  def debit(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient balance")

  def display(self):
    print(f"Account Number: {self.account_number}")
    print(f"Account Type: {self.account_type}")
    print(f"Account Balance: {self.balance}")

class CreditAccount(Account):
  def __init__(self, account_number, credit_limit):
    super().__init__("credit", account_number, 0)
    self.credit_limit = credit_limit

  def debit(self, amount):
    if amount <= self.credit_limit:
      super().debit(amount)
    else:
      print("Insufficient credit limit")

  def display(self):
    super().display()
    print(f"Credit Limit: {self.credit_limit}")

class DebitAccount(Account):
  def __init__(self, account_number, balance):
    super().__init__("debit", account_number, balance)


class HybridAccount(CreditAccount, DebitAccount):
  def __init__(self, account_number, credit_limit, balance):
    Account.__init__(self, "hybrid", account_number, balance)
    CreditAccount.credit_limit = credit_limit

  def display(self):
    CreditAccount.display(self)

def create_credit_account(customer):
  print(f"Creating credit account for {customer.name} with email {customer.email}")
  account_number = random.randint(1, 1000)
  account = CreditAccount(account_number, 100)
  customer.add_account(account)

def create_debit_account(customer):
  initial_deposit = int(input("Enter the initial deposit: "))
  while initial_deposit <= 0:
    initial_deposit = int(input("Invalid amount. Please enter deposit greater than 0:"))
  print(f"Creating debit account for {customer.name} with email {customer.email}")
  account_number = random.randint(1, 1000)
  da = DebitAccount(account_number, initial_deposit)
  customer.add_account(da)

def create_hybrid_account(customer):
  initial_deposit = int(input("Enter the initial deposit: "))
  while initial_deposit < 0:
    initial_deposit = input("Invalid amount. Please enter deposit 0 or greater than 0:")
  print(f"Creating hybrid account for {customer.name} with email {customer.email}")
  account_number = random.randint(1, 1000)
  ha = HybridAccount(account_number, 100, initial_deposit)
  customer.add_account(ha)

def create_account(customer):
  # Prompt the user to enter the option
  account_option = input('''Why type of Account you like to create?
  1. Credit Account
  2. Debit Account
  3. Hybrid Account
  ''')

  if account_option == '1':
    create_credit_account(customer)
    return customer
  elif account_option == '2':
    create_debit_account(customer)
    return customer
  elif account_option == '3':
    create_hybrid_account(customer)
    return customer
