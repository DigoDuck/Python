# Itertools
# Combinations, Permutations e Product
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

pessoas = [
    "João", "Pietro", "Michele", "Ana"
]
camisetas = [
    ["Preta", "Branca"],
    ["P", "M", "G"],
    ["Masculino", "Feminino", "Unisex"],
    ["Algodão", "Linho"],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))