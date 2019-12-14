
class Person:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def greet(self):
        my_name = self.name
        print(f'hello my name is {my_name}')

person1 = Person(name="jack", age=31, location="Queens")
person2 = Person(name="joaquin", age=30, location="Brooklyn")



if person1.name == "jack":
    print("his name is jack")
elif person1.name == "joaquin":
    print("his name is joaquin")
else:
    print("that name was not defined")

'''import pdb; pdb.set_trace()'''

