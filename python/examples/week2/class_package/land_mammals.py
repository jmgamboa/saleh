from .mammals import Mammal

class Bear(Mammal):
    
    def greet(self):
        super().greet()
        print('Roar') 
