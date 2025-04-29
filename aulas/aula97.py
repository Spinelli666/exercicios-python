# Como importar coisas do seu próprio módulo (ponto de vista do __main_)

import aula97_m
from aula97_m import soma, variavel_modulo

# print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))