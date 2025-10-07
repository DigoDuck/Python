entrada = input("[E]ntrar [S]sair: ")
senha = input("senha")

senha_permitida = "123456"

if entrada == "E" and senha == senha_permitida:
    print("Entrar")
else:
    print("Sair")