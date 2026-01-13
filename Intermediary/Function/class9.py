

def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}"
    return saudar


s1 = criar_saudacao("Bom dia", "Diogo")
print(s1())