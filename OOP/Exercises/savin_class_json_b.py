import json

from savin_class_json import PATH_FILE, Person

with open(PATH_FILE, 'r') as a_file:
    people = json.load(a_file)
    p1 = Person(**people[0]) 
    p2 = Person(**people[1]) 
    p3 = Person(**people[2])
    
print(p1.name)
print(p2.name)
print(p3.name)