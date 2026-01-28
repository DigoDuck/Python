# Scope of the class ans its methods

class Animal:
    # name = "Lion"

    def __init__(self, name):
        self.name = name
        
        variable = "value"
        print(variable)
        
    def eating(self, food):
        return f"{self.name} is eating {food}"
        
lion = Animal(name="Lion")
print(lion.name)
print(lion.eating("meat"))