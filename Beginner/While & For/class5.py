nome = "Diogo Ribeiro"

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

nova_string = ""
indice = 0

while indice < len(nome):
    letra = nome[indice]
    nova_string += f"*{letra}"
    indice += 1

print(nova_string)