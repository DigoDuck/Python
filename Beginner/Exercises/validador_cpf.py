import re
import sys

# cpf_env_user = "746.824.890-70" \
#     .replace(".", "") \
#     .replace("-", "") \
#     .replace(" ", "")

entrada = input("Digite o CPF: [746.824.890-70] ")
cpf_env_user = re.sub(
    r"[^0-9]",
    "",
    entrada
    )

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print("Você enviou dados sequenciais")
    sys.exit()

nove_digitos = cpf_env_user[:9]
contador_regressivo_1 = 10

resultado_d1 = 0
for digito in nove_digitos:
    resultado_d1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_d1 * 10 % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_d2 = 0
for digito in dez_digitos:
    resultado_d2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_d2 * 10 % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_res = f"{ nove_digitos}{ digito_1}{digito_2}"

if cpf_env_user == cpf_res:
    print(f"{ cpf_env_user} é válido")
else:
    print("CPF INVÁLIDO")