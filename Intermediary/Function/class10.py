pessoa = {
    "nome": "Diogo",
    "sobrenome": "Mota",
    "idade": 21,
    "altura": 1.8,
    "endereços": [
        {"rua": "exemplo de rua", "número": 10},
        {"rua": "exemplo de outra rua", "número": 1},
    ]
}

print(pessoa["endereços"])

for chave in pessoa:
    print(chave, pessoa[chave])