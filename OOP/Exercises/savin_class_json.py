import json

PATH_FILE = "OOP\Exercises\saving_class.json"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
p1 =  Person ("Jonnas", 37)
p2 =  Person ("Hellen", 9)
p3 =  Person ("Paula", 22)
db = [vars(p1),  p2.__dict__, vars(p3)]

def do_dump():
    with open(PATH_FILE, 'w') as  a_file:
        json.dump(db, a_file,  ensure_ascii=False, indent=2)