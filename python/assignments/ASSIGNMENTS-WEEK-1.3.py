'''Given these items and prices
    banana: price:4, inventory: 3
    apple: price:2, inventory 2
    orange: price 1.5, inventory 4
    pear: price 3, inventory 2

    Write a program that promps the user for an item. The output will be the items price and inventory amount'''

Order = input(
    '(Menu: banana, apple, orange, pear)\n What fruit would you like? ')

banana = {
    'Price': 4,
    'Inventory': 3
}
apple = {
    'Price': 2,
    'Inventory': 2
}
orange = {
    'Price': 1.5,
    'Inventory': 4
}
pear = {
    'Price': 3,
    'Inventory': 2
}

if Order == 'banana':
    print(banana)
elif Order == 'apple':
    print(apple)
elif Order == 'orange':
    print(orange)
elif Order == 'pear':
    print(pear)
else:
    print('Sorry we don\'t have that')
