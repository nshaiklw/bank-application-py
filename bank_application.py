
import bank_utils

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
      new_account = bank_utils.create_account()
      if new_account:
        print("\nAccount created successfully!")
        new_account.display()
        print("-" * 20)
  elif option == '2':
      print('Check Balance')
  elif option == '3':
      print('Deposit')
  elif option == '4':
      print('Withdrawl')

print("Thank you, visit Again!")
