frase = "O python é uma linguagem de programação Multiparadigma. " \
    "Python foi criadopor Guido."

i = 0
qnt_mais_vzs = 0
letra_q_apr = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qnt_letra = frase.count(letra_atual)

    if qnt_mais_vzs < qnt_letra:
        qnt_mais_vzs = qnt_letra
        letra_q_apr = letra_atual


    # print(letra_atual, qnt_letra)
    i += 1
print(letra_q_apr, qnt_mais_vzs + 1)
