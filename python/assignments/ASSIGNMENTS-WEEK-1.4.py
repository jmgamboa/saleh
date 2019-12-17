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


class BankAccount:

    def __init__(self, user, passcode, balance):
        self.user = user
        self.passcode = passcode
        self.balance = int(balance)

    def deposit(self, code, amount):
        if code == self.passcode:
            self.balance += int(amount)
            print(f'Deposit granted')
        else:
            print(f'Invalid code, try again')

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


commands = ['new account', 'deposit', 'withdraw', 'balance', 'exit']
exit = False
while exit == False:
    command = input(
        f'What would you like to do?\n new account\n deposit\n withdraw\n balance\n exit\nPlease enter your command: ')
    if command == commands[0]:  # Create new account
        username = input(f'Enter username: ')
        passcode = input(f'Enter passcode: ')
        balance = input(f'Insert balance: ')
        account = BankAccount(username, passcode, balance)
    elif command == commands[1]:
        # this inputs and pass results to deposit
        result = (input(f'Please enter passcode: '),
                  input(f'Please insert deposit amount: '))
        # this calls the function
        account.deposit(code=result[0], amount=result[1])
    elif command == commands[2]:
        result = (input(f'Please enter passcode: '),
                  input(f'Please insert withdraw amount: '))
        account.withdraw(code=result[0], amount=result[1])
    elif command == commands[3]:
        print(balance)
    else:
        command == commands[4]
        exit = True
