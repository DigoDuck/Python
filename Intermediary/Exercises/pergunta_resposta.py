perguntas = [
    {
        "Pergunta": "Quanto é 2 + 2?",
        "Opções": ["1", "2", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5 * 5?",
        "Opções": ["15", "25", "10", "51", "55"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10 / 2?",
        "Opções": ["4", "2", "5", "4", "7"],
        "Resposta": "5",
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()

    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print("Acertou🤙")
    else:
        print("Errou😬")

    print()

print("Você acertou ", qtd_acertos)
print("de", len(perguntas), "perguntas")