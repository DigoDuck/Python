# raise - lançando exceções (erros)
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Não pode dividir por zero")
    return True

def deve_ser_int_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f"{n} deve ser int ou float"
        )
    return True

def divide(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, "0"))