import csv
from class_package import land_mammals
from class_package.sea_mammals import Whale

with open('mammals.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    counter = 0
    amount_of_mammals_with_hair = 0
    for row in spamreader:
        if row[2] == 'true':
            amount_of_mammals_with_hair += 1

bear = land_mammals.Bear()
whale = Whale()
# print(f'mamals with hair {amount_of_mammals_with_hair}')