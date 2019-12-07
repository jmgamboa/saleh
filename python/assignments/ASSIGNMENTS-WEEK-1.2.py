# Write a program that takes 2 lists and returns a new list that contains all the elements of the first list minus all the duplicates.

# Stores a list in []
inputList1 = []
# Asks user for numbers and to separate with a ,
numbers = input('Input your numbers: ')
# For loop for every entry number to be added as integer in inputList1
for entry in numbers:
    inputList1.append(int(entry))

# Repeated method from inputList1
inputList2 = []
numbers = input('Input your numbers again: ')
for entry in numbers:
    inputList2.append(int(entry))

# Added numbers from inputList1 and inputList2 to make a newList
newList = (inputList1 + inputList2)

# Use for loop separate the duplicate numbers and unique numbers from newList
dup_nums = set()
uniq_nums = []
for nums in newList:
    if nums not in dup_nums:
        uniq_nums.append(nums)
        dup_nums.add(nums)

# Output the unique numbers from newList
print(uniq_nums)
