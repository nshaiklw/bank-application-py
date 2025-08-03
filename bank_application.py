
import bank_utils
import random
import importlib
import pickle
importlib.reload(bank_utils)

customers = {}
try:
    with open("accounts_data.pkl", "rb") as f:
        customers = pickle.load(f)
except FileNotFoundError:
    pass

def get_customer():
  existing_customer = input("Are you an existing customer? (yes/no): ")
  if existing_customer.lower() == 'yes':
    customer_number = input("Please enter your customer number: ")
    if customer_number not in customers:
      customer_number = input("Customer is invalid, please retry")
    return customers[customer_number]


print("Welcome to Bank of Python!")
option = 0
while option != '5':
  # Prompt the user to enter the option
  option = input('''How may I help you? Please choose the option
  1. Create an account
  2. Check Balance
  3. Deposit
  4. Withdrawl
  5. Exit
  ''')

  if option == '1':
    customer = get_customer()
    if customer:
      customer.display()
      print("-" * 20)
    else:
      customer_number = str(random.randint(1, 1000))
      name = input("Please enter your name: ")
      email = input("Please enter your email: ")
      customer = bank_utils.Customer(customer_number, name, email)
      customer.display()
    bank_utils.create_account(customer)
    customers[customer.customer_number] = customer
    print("\nAccount created successfully")
    customer.display()
    print("-" * 20)
  elif option == '2':
    customer = get_customer()
    if customer:
      customer.display()
      print("-" * 20)
  elif option == '3':
    customer = get_customer()
    if customer:
      customer.display()
      print("-" * 20)
      account_number = input("Enter the account number")
      account = customer.accounts[int(account_number)]
      amount = input("Enter the amount")
      account.credit(int(amount))      
  elif option == '4':
    customer = get_customer()
    if customer:
      customer.display()
      print("-" * 20)
      account_number = input("Enter the account number")
      account = customer.accounts[int(account_number)]
      amount = input("Enter the amount")
      account.debit(int(amount))      

# Store the dictionary in a file
with open("accounts_data.pkl", "wb") as f:
  pickle.dump(customers, f)

print("Thank you, visit Again!")
