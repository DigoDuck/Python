# Empacotamento e Desempacotamento

a, b = 1, 2
a, b = b, a

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza"
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# (a1, a2), b = pessoa.items()
# print(a1, a2,)
# print(b)

def mostro_argumentos(*args, **kwargs):
    print(kwargs)

mostro_argumentos(nome="Joana", qlq=123)