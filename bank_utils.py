import bank_utils
import random
import importlib
importlib.reload(bank_utils)


customers = {}

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
      customer = bank_utils.create_account()
      if customer is not None:
        if customer.customer_number not in customers:
          customers[customer.customer_number] = customer
        print("\nAccount created successfully!")
        customer.display()
        print("-" * 20)
  elif option == '2':
      print('Check Balance')
  elif option == '3':
      print('Deposit')
  elif option == '4':
      print('Withdrawl')

print("Thank you, visit Again!")
