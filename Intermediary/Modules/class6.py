from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Wagner', 'nota': 'A'},
    {'nome': 'Matheus', 'nota': 'C'},
    {'nome': 'Marcela', 'nota': 'D'},
    {'nome': 'Fernanda', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Paula', 'nota': 'A'},
    {'nome': 'Vitor', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_sgrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos, key=ordena)


for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)