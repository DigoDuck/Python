def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        #
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string("Diogo")
print(invertida)