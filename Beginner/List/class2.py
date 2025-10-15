lista = [1, 2, 3, 4]
# lista[0] = 10
# del lista[0]
# print(lista[0])
# print(lista)
lista.append(5)
lista.append(6)
lista.append("BBB")
ultimo_valor = lista.pop()
lista.pop()
print(lista, "Removido:", ultimo_valor)