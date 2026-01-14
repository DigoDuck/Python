primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

if valor1 > valor2:
    print(f"{valor1= } é maior que {valor2= }")
elif valor1 < valor2:
    print(f"{valor2= } é menor que {valor1= }")
else:
    print("Os valores são iguais!")