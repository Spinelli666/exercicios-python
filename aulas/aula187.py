# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fire Code

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Nenhum argumento foi passado.')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com o {argumentos[1]}')
        print(f'Faça outra coisa com o {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')