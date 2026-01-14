# Dictionary Comprehension e Set Comprehension

produto = {
    "nome": "Copo",
    "preco": 2.5,
    "categoria": "Cozinha",
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

s1 = {2 ** i for i in range(10)}
print(s1)