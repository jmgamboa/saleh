# Write a class that enables you to create a BankAccount
#    Instantiating this BackAccount will allow you to set the balance of the bank account

#    ie

#    new_account = BankAccount(balance=1000)
#    new_account2 = BankAccount(balance=2000)

#    The class should implement functions that allow you to withdraw and deposit more to the balance
#    the withdraw minimum has to be at least 10 dollars, with an added fee of 2 dollars applied to the balance
#    You cannot withdraw more than the balance plus the fee. (You cannot over draft). If the user attempts to, the programs alerts the user of insufficient funds

#    For the sake of simplicity do not worry about decimals / floats.

#    inspecting an instantiated objects balance should reflect the correct balance

import pdb


class BankAccount:

    def __init__(self, user, passcode, balance):
        self.user = user
        self.passcode = passcode
        self.balance = balance

    def deposit(self, code, amount):
        if code != self.passcode:
            print(f'Invalid code, try again')
        else:
            self.balance += amount
            print(f'Deposit granted')

    def withdraw(self, code, amount):
        if code == self.passcode:
            fee = 2
            if amount <= 10:
                print(f'Minimum withdraw is 10 plus 2 fee')
            elif amount <= self.balance:
                self.balance -= amount
                self.balance -= fee
                print(f'Withdraw granted')
            else:
                print(f'Insufficient funds')
        else:
            print(f'Invalid code, try again')


commands = ['exit', 'new account', 'deposit', 'withdraw']
exit = False
while exit == False:
    command = input(
        f'What would you like to do?\n Exit\n New account\n Deposit\n Withdraw\n Please enter your command: ')
    if command == commands[0]:
        exit = True
    elif command == commands[1]:  # Create new account
        username = input(f'Enter Username: ')
        passcode = input(f'Enter Passcode: ')
        balance = input(f'Insert balance: ')
        account = BankAccount(username, passcode, balance)
    elif command == commands[2]:
        result = (input(f'Please enter passcode: '),
                  input(f'Please insert deposit amount: '))#this inputs and pass results to deposit
        account.deposit(code=result[0], amount=result[1])#this calls the function 
    elif command == commands[3]:
        account.withdraw = (input(f'Please enter passcode: '))
