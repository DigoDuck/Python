p1 = {
    "Nome": "Diogo",
    "Sobrenome": "Mota",
}

# nome = p1.pop('Nome')
# print(nome)
# print(p1)

# nome = p1.popitem()
# print(nome)
# print(p1)


# p1.update({
#     "Nome": "Novo valor"
# })
# print(p1)

# p1.update(nome="novo valor", idade=20)

tupla = ("nome", "novo valor"), ("idade", 20)
p1.update(tupla)
print(p1)