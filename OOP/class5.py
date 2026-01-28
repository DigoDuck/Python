# class attributes

class Person:
    current_year = 2026

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def year_birth(self):
        return Person.current_year - self.age
    

p1 = Person("Jonas", 37)
p2 = Person("Jess", 19)
p3 = Person("Diogo", 21)

print(p1.year_birth())
print(p2.year_birth())
print(p3.year_birth())