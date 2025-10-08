# nome = "Diogo"

# print(nome[-5])

# print("Di" in nome)
# print("Dg" in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que quer encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em { nome}")