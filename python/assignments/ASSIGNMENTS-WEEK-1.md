                                                                                                                                                                                                                                                                                                                                                                                                      Setup

Setup git https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup. Create new directory called solutions within saleh/python/assignments/solutions and make a .py file for each of the solutions within the solutions directory.

Install pyenv and use a more later version of python https://github.com/pyenv/pyenv#installation

0. Write a program that takes a user input which is a number and the program outputs whether it is even or odd
 
1. Write a program that prompts two different questions. First asks the users name. The second asks the year they were born. The output of the program greets the user by name, states their age, and if they are old enough to drink in the United States

2. Write a program that takes 2 lists and returns a new list that contains all the elements of the first list minus all the duplicates. 

ex 
first list [1, 2, 3, 4, 5]
second list [2, 3, 4, 5]

output = [1]


3. Given these items and prices
    banana: price:4, inventory: 3
    apple: price:2, inventory 2
    orange: price 1.5, inventory 4
    pear: price 3, inventory 2

    Write a program that promps the user for an item. The output will be the items price and inventory amount

4. Write a class that enables you to create a BankAccount
   Instantiating this BackAccount will allow you to set the balance of the bank account

   ie 

   new_account = BankAccount(balance=1000)
   new_account2 = BankAccount(balance=2000)

   The class should implement functions that allow you to withdraw and deposit more to the balance
   the withdraw miminum has to be at least 10 dollars, with an added fee of 2 dollars applied to the balance
   You cannot withdraw more than the balance plus the fee. (You cannot over draft). If the user attemps to, the programs alerts the user of insufficient funds

   Also implement a username and pincode to your class such that you can not withddraw or deposit money if the username an pincode are incorrect

   For the sake of simplicity do not worry about decimals / floats. 

   inspecting an insantiated objects balance should reflect the correct balance

   Part 2

   Leveraging your class, write a program that allows you to input commands: Exit, Withdraw, Deposit

   The program prompts a user to create an account with a username and password. They then can provide which commands they want and perform the correlating action. Withdraw accepts username and pincode and performs the draw of funds to the balance and deposit prompts for the same parameters but puts money into the balance. Exit command will exit. 



