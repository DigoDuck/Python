

try:
    print("Abrir arquivo")
    # a
except Exception as err:
    print(err)
else:
    print("Não deu erro")
finally:
    print("Fechar arquivo")