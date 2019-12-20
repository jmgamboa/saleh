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
        self.balance = balance

    def deposit(self, code, amount):
        if code == self.passcode:
            self.balance += amount
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

        return self.balance


new_account = BankAccount('Jack', 1234, 1000)
new_account.deposit(5555, 200)
new_account.withdraw(1234, 10)
print(new_account.balance)
