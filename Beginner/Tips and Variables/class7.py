nome = "Diogo"
sobrenome = "Motta"
Idade = 21
altura = 1.87
ano_nascimento = 2025 - Idade
maior_de_idade = Idade >= 18
altura_metros = 1.80
peso_kg = 108
imc = peso_kg / int(altura_metros ** 2)

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", Idade)
print("Altura:", altura)
print("Ano de Nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura_metros)
print("Peso em kg:", peso_kg)
print("IMC:", imc)