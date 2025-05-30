# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        print(f'O resultado é {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__} foi chamada')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('O parâmetro deve ser uma string')
    return True

invertida = inverte_string('123')
print(invertida)