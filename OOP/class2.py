# Methods in class instances in Python

class Car:
    def __init__(self, name):
        self.name = name
        
    def accelerate(self):
        print(f"{self.name} is accelerating...")
        
porsche = Car(name="Porsche")
print(porsche.name)
porsche.accelerate()
print()
lamborghini = Car(name="Lamborghini")
print(lamborghini.name)
lamborghini.accelerate()