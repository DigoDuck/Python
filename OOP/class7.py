# Class Method + factories

class Person:
    year = 2026 # class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def class_method(cls):
        print("Hey")
    
    @classmethod
    def create_with_age_50(cls, name):
        return cls(name, 50)
    
    @classmethod
    def create_nameless(cls, age):
        return cls("Anonymous", age)
        
p1 = Person("Dennis", 24)
p2 = Person.create_with_age_50("José")
p3 = Person.create_nameless(23)
print(p2.name, p2.age)
print(p3.name, p3.age)