"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Minhas Respostas:

# numero = input("Digite um número para verificar ser é par ou impar: ")

# if numero.isdigit():
#     numero_int = int(numero)

#     if numero_int % 2 == 0:
#         print(f"O número {numero} é par")
#     elif numero_int % 2 >= 1:
#         print(f"O número {numero} é impar")
# else:
#     print("Você não digitou um número")


# hora = float(input("Digite o horário em números float: "))

# if hora <= 11.00:
#     print("Bom dia!")
# elif hora <= 17.00:
#     print("Boa tarde!")
# else:
#     print("Boa noite!")

# nome = input("Digite seu nome: ")

# if len(nome) <= 4:
#     print("Seu nome é curto")
# elif len(nome) <=6:
#     print("Seu nome é normal")
# else:
#     print("Seu nome é muito grande")


# Respostas:
# numero = input("Digite um número inteiro: ")

# try:
#     conversao_inteiro = int(numero)
# except:
#     print("Isso não é um número inteiro")

# if conversao_inteiro % 2 == 0:
#     print("O número é Par")
# elif conversao_inteiro % 2 != 0:
#     print("O número é ímpar")


# horas = input("Que hora é: ")
# horas_int = int(horas)

# if horas_int >= 0 and horas_int <= 11:
#     print('Bom dia!')
# elif horas_int > 11 and horas_int <= 17:
#     print('Boa tarde!')
# elif horas_int > 17 and horas_int <= 23:
#     print('Boa noite!')

# #Exercício 3:
# nome = input("Digite o seu primeiro nome: ")

# if len(nome) <= 4:
#     print("Seu nome é curto")
# elif len(nome) >= 5 and len(nome) <= 6:
#     print("Seu nome é normal")
# else:
#     print("Seu nome é muito grande")