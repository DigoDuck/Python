# __dict__ and vars for instance attributes

class Person:
    current_year = 2026

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def year_birth(self):
        return Person.current_year - self.age
    
data = {'name': 'Jonas', 'age': 37}    

p1 = Person(**data)
# p1.__dict__["other"] = "thing"
# print(p1.__dict__)
# print(vars(p1))
# print(p1.other)

print(vars(p1))
print(p1.name)