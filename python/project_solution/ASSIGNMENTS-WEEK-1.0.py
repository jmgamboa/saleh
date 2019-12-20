# Python Program to check if the input number is odd or even.

# Ask user for number
num = int(input('Enter a number: '))
# Checks if the number input is even or odd.(Using a if else statement)
if (num % 2) == 0:
    print(f'{num} is Even')
else:
    print(f'{num} is Odd')
