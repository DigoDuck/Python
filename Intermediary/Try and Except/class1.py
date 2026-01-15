# Try, except, else e finally

a = 18
b = "a"

try:
    
    c = a / b
except ZeroDivisionError:
    print("Tentou dividir por zero")
except NameError:
    print("Alguma variavel não foi definida")
except Exception as error:
    print("Erro desconhecido")
    print(error)
    
print("Continuar")