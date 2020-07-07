class BankAccount:

    def __init__(self, user, passcode, balance, acc_bank):
        self.user = user
        self.passcode = passcode
        self.balance = balance
        self.acc_bank = acc_bank

    def deposit(self, code, amount):
        if code == self.passcode:
            self.balance += amount
            print(f'Your deposit is granted of {amount}. Your balance is {self.balance}.')
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
                print(f'Your withdrawl is granted of {amount}. Your balance is {self.balance}.')
            else:
                print(f'Insufficient funds')
        else:
            print(f'Invalid code, try again')
        

    def display(self, code):
        if code == self.passcode:
            print(f'Your available balance is {self.balance}.')
        else:
            print(f'Invalid code, try again')


#        - you can also perform the other actions on checking / saving as well
#        (check balance, withdraw)
class BofA(BankAccount):

    checking = 0
    savings = 0

    def __init__(self, user, passcode, balance):
        super().__init__(user, passcode, balance, acc_bank)


    def deposit(self, code, amount, acct_type):
        if code == self.passcode:
            
            if acct_type == 1:
                self.balance += amount
                BofA.checking += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {BofA.checking}.')
            elif acct_type == 2:
                self.balance += amount
                BofA.savings += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {BofA.savings}.')
            else:
                print(f'Invalid number, try again.')
        else:
            print(f'Invalid code, try again.')


    def withdraw(self, code, amount, acct_type):
        if code == self.passcode:
            #Check if there is funds available if not then print no funds else which account user wants to withdraw (1 = checking or 2 = savings).
            if acct_type == 1:
                if self.balance == 0 and BofA.checking == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    BofA.checking -= self.balance
                    print(f'Your withdrawal is granted of {amount}. Your balance is {BofA.checking}.')
            elif acct_type == 2:
                if self.balance == 0 and BofA.savings == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    BofA.savings -= self.balance
                    print(f'Your withdrawl is granted of {amount}. Your balance is {BofA.savings}.')
            else:
                print(f'Invalid number, try again.')
        else:
            print(f'Invalid code, try again')

    def display(self, code, acct_type):
        pass        

class Chase(BankAccount):

    checking = 0
    savings = 0

    def __init__(self, user, passcode, balance):
        super().__init__(user, passcode, balance, acc_bank)

    
    def deposit(self, code, amount, acct_type):
        if code == self.passcode:

            if acct_type == 1:
                self.balance += amount
                Chase.checking += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {Chase.checking}.')
            elif acct_type == 2:
                self.balance += amount
                Chase.savings += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {Chase.savings}.')
            else:
                print(f'Invalid number, try again.')
        else:
            print(f'Invalid code, try again.')



    def withdraw(self, code, amount, acct_type):
        if code == self.passcode:     
            if acct_type == 1:
                if self.balance == 0 and Chase.checking == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    Chase.checking -= self.balance
                    print(f'Your withdrawal is granted of {amount}. Your balance is {Chase.checking}.')
            elif acct_type == 2:
                if self.balance == 0 and Chase.savings == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    Chase.savings -= self.balance
                    print(f'Your withdrawal is granted of {amount}. Your balance is {Chase.savings}.')
            else:
                print(f'Invalid number, try again.')
        else: 
            print(f'Invalid code, please try again.')

    def display(self, code, acct_type):
        pass

class TD(BankAccount):

    checking = 0
    savings = 0

    def __init__(self, user, passcode, balance):
       super().__init__(user, passcode, balance, acc_bank)

    def deposit(self, code, amount, acct_type):
        if code == self.passcode:

            if acct_type == 1:
                self.balance += amount
                TD.checking += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {TD.checking}.')
            elif acct_type == 2:
                self.balance += amount
                TD.savings += self.balance
                print(f'Your deposit is granted of {amount}. Your balance is {TD.savings}.')
            else:
                print(f'Invalid number, try again.')
        else:
            print(f'Invalid code, try again.')

    def withdraw(self, code, amount, acct_type):
        if code == self.passcode:
            fee = 3
            #change to TD and add fee to each withdraw
            import pdb; pdb.set_trace()
            if acct_type == 1:
                if self.balance == 0 and TD.checking == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    self.balance -= fee
                    TD.checking -= self.balance
                    print(f'Your withdrawal is granted of {amount}. Your balance is {TD.checking}.')
            elif acct_type == 2:
                if self.balance == 0 and TD.savings == 0:
                    print(f'You have no funds in your account.')
                else:
                    self.balance -= amount
                    self.balance -= fee
                    TD.savings -= self.balance
                    print(f'Your withdrawal is granted of {amount - fee}. Your balance is {TD.savings}.')
            else:
                print(f'Invalid number, try again.')
        else:
            print(f'Invalid code, try again')
   
    def display(self, code, acct_type):
        pass        

commands = ['new account', 'log in', 'deposit', 'withdraw', 'balance', 'exit']
exit = False
while exit == False:
    command = input(
        f'What would you like to do?\n new account\n log in \n deposit\n withdraw\n balance\n exit\nPlease enter your command: ')
    if command == commands[0]:
        #creates new user account and stores in a dict
        accounts = {}        
        New_account = True
        while New_account:
            
            username = input(f'Enter username: ')
            passcode = input(f'Enter passcode: ')
            balance = int(input(f'Insert balance: '))
            acc_bank = int(input(f'What bank account would you like to open?\n 1 for BofA\n 2 for Chase\n 3 for TD\n Please enter bank account number: '))
             
            if acc_bank == 1:
                accounts[username] = BofA(username, passcode, balance)
            elif acc_bank == 2:
                accounts[username] = Chase(username, passcode, balance)
            elif acc_bank == 3:
                accounts[username] = TD(username, passcode, balance)
            else:
                print(f'You did not enter a valid bank account number, please try again.')
             

            repeat = input(f'Do you want to add another account? ').lower()
            if repeat == 'no' or 'n':
                New_account = False
    elif command == commands[1]:
        #Checks if user already exists and is in accounts
        login = input(f'Please Enter username: ')
        if login in accounts:
            print(username)
            print(f'Username already exists.')
        else:
            print(f'Username doesn\'t exist, Please make a new account.')
    elif command == commands[2]:
        # this inputs and pass results to deposit
        result = (input(f'Please enter passcode: '),
        int(input(f'What account do you want to deposit to\n 1 = Checking\n 2 = Savings\n Enter your account number: ')), int(input(f'Please insert deposit amount: ')))
        # this calls the function
        accounts[username].deposit(code=result[0], acct_type=result[1], amount=result[2])
    elif command == commands[3]:
        result = (input(f'Please enter passcode: '), int(input(f'What account do you want to deposit to\n 1 = Checking\n 2 = Savings\n Enter your account number: ')), int(input(f'Please insert withdraw amount: ')))
        accounts[username].withdraw(code=result[0],
        acct_type=result[1], amount=result[2])
    elif command == commands[4]:
        result = (input(f'Please enter passcode: '))
        accounts[username].display(code=result)
    else:
        command == commands[5]
        exit = True