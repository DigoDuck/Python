# class - Classes are templates for creanting new objects

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
p1 = Person("Diogo", "Motta")
# p1.name = "Diogo"
# p1.surname = "Motta"

p2 = Person("Felícia", "França")
# p2.name = "Felícia"
# p2.surname = "França"

print(p1.name)
print(p1.surname)
print()
print(p2.name)
print(p2.surname)