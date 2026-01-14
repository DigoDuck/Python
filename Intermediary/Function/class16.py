# Introdução á função lambda + list.sort e sorted

lista = [
    {"Nome": "Diogo", "Sobrenome": "Ribeiro"},
    {"Nome": "Flávio", "Sobrenome": "Figueiredo"},
    {"Nome": "Anna", "Sobrenome": "Silva"},
    {"Nome": "Monique", "Sobrenome": "Almeida"},
]

# def ordena(item):
#     return item["Nome"]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item["Nome"])
l2 = sorted(lista, key=lambda item: item["Sobrenome"])

exibir(l1)
exibir(l2)