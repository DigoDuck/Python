import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)
# print(list(range(10)))

# Mapeamento de dados em list comprehension
produtos = [
    {"nome": "p1", "preco": 20,},
    {"nome": "p2", "preco": 10,},
    {"nome": "p3", "preco": 50,},
]
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
    if produto["preco"]> 10
]
p(novos_produtos)
