import json

# person = {
#     "name": "Diogo Ribeiro",
#     "surname": "Motta",
#     "address": [
#         {"street": "S1", "number": 55},
#         {"street": "S2", "number": 7},
#     ],
#     "height": 1.8,
#     "favorite numbers": (5,777,17),
#     "dev": True,
#     "nothing": None,
# }

# with open("class3.json", 'w', encoding="utf8") as a_file:
#     json.dump(
#         person, 
#         a_file,
#         ensure_ascii=False,
#         indent=2,
#     )

with open("class3.json", 'r', encoding="utf8") as a_file:
    person = json.load(a_file)
    print(person)
    print(type(person))
    print(person["name"])