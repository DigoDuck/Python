def mult(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = mult(5,5,5)
print(multiplicacao)

def par_impar(num):
    if num % 2 == 0:
        print("é par")
    else:
        print("É ímpar")

par_impar(61)