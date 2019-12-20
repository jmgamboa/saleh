# Write a program that prompts two different questions. First asks the users name. The second asks the year they were born. The output of the program greets the user by name, states their age, and if they are old enough to drink in the United States
# Python Program ask for User name, year there born and if there legal to drink in the US.

# Ask user to input name
name = str(input('Hello, what is your name? '))
# Ask user to input year there born
year = int(input('What year were you born? '))

# Takes input of born year and subtracts with current year to get users age
current_year = 2019
age = (current_year - year)

# Output greet with user's name
print(f'Hello {name}')
# Output user's age
print(f'{age} years old')

# I/O of user's age to check if their legal to drink in the US
if age >= 21:
    print('Legal')
else:
    print('Not Legal')
