# import sys
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula99_package
# Não faz nada, melhor fazer isso
#import aula99_package.modulo
#from aula99_package.modulo import soma_do_modulo
#from aula99_package import modulo
# from aula99_package.modulo import *

# print(__name__)
# print(*sys.path, sep='\n')

# print(soma_do_modulo(1, 2))
#print(aula99_package.modulo.soma_do_modulo(1, 2))
#print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula99_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()

import aula99_package

print(aula99_package.soma_do_modulo(2, 3))
print()
aula99_package.fala_oi()