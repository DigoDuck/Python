def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (l1[i], l2[i]) for i in range(intervalo_maximo)
    ]
    
from itertools import zip_longest
    
l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]
# print(zipper(l1, l2))
print(list((zip(l1, l2))))
print(list((zip_longest(l1, l2, fillvalue="Cidade não informada."))))