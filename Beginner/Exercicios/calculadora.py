""" Calculadora com While """


while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input("Digite o operador (+ - / *):")


    numeros_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue

    operadores_permitidos = "+-/*"

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    if operador not in operadores_permitidos:
        print("Operador Inválido")
        continue

    if operador == "+":
        resultado = num1_float + num2_float
    elif operador == "-":
        resultado = num1_float - num2_float
    elif operador == "/":
        if num2_float == 0:
            print("Não se pode dividir nenhum número por 0")
            continue
        resultado = num1_float / num2_float
    elif operador == "*":
        resultado = num1_float * num2_float
    else:
        print("O que diabos aconteceu????")

    print(f"o resultado do cálculo é: {resultado}")

    sair = input("Quer sair? ").lower().startswith("s")
    

    if sair:
        break