from functools import reduce

# reduce 
produtos = [
    { "nome": "Produto 5", "preco": 10},
    { "nome": "Produto 1", "preco": 22},
    { "nome": "Produto 3", "preco": 2},
    { "nome": "Produto 2", "preco": 6},
    { "nome": "Produto 4", "preco": 4},
]

def funcao(acumulador, produto):
    print(acumulador)
    print()
    return acumulador + produto["preco"]
    
total = reduce(
    funcao,
    produtos,
    0
)

print(total)