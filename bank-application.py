def create_account():
  # Prompt the user to enter the option
  account_option = input('''Why type of Account you like to create?
  1. Credit Account
  2. Debit Account
  3. Hybrid Account
  ''')
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  if account_option == '1':
    create_credit_account(name, email)    
  elif account_option == '2':
    create_debit_account(name, email)
  elif account_option == '3':
    create_hybrid_account(name, email)


def create_credit_account(name, email):
  print(f"Creating credit account for {name} with email {email}")

def create_debit_account(name, email):
  initial_deposit = int(input("Enter the initial deposit: "))
  print('Inital deposit', initial_deposit)
  while initial_deposit <= 0:
    initial_deposit = int(input("Invalid amount. Please enter deposit greater than 0:"))
  print(f"Creating debit account for {name} with email {email}")

def create_hybrid_account(name, email):
  initial_deposit = input("Enter the initial deposit: ")
  while initial_deposit < 0:
    initial_deposit = input("Invalid amount. Please enter deposit 0 or greater than 0:")
  print(f"Creating hybrid account for {name} with email {email}")


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
      create_account()
  elif option == '2':
      print('Check Balance')
  elif option == '3':
      print('Deposit')
  elif option == '4':
      print('Withdrawl')

print("Thank you, visit Again!")