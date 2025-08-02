import bank_utils
import random
import importlib
import json
importlib.reload(bank_utils)


class BankEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bank_utils.Customer, bank_utils.Account)):
            return obj.__dict__
        return super().default(obj)

def customer_decoder(obj):
    if 'customer_number' in obj and 'name' in obj and 'email' in obj:
        customer = bank_utils.Customer(obj['customer_number'], obj['name'], obj['email'])
        for account_number, account_data in obj['accounts'].items():
            # Here you would add logic to decode the different account types
            # For now, we'll just create a generic Account object
            account = bank_utils.Account(account_number)
            customer.add_account(account)
        return customer
    return obj

customers = {}
try:
    with open("accounts_data.json", "r") as f:
        customers = json.load(f, object_hook=customer_decoder)
except FileNotFoundError:
    pass


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
      customer, new_account = bank_utils.create_account()
      if customer and new_account:
        if customer.customer_number not in customers:
          customers[customer.customer_number] = customer
        # The add_account method is already called inside the create_*_account functions
        # So we don't need to call it again here.
        print("\nAccount created successfully!")
        customer.display()
        print("-" * 20)
  elif option == '2':
      print('Check Balance')
  elif option == '3':
      print('Deposit')
  elif option == '4':
      print('Withdrawl')

# Store the dictionary in a file
with open("accounts_data.json", "w") as f:
  json.dump(customers, f, cls=BankEncoder, indent=4)

print("Thank you, visit Again!")
