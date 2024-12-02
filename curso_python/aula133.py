# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protect = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protect)
        print(self.__private)
        self.__metodo_privated()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_privated(self):
        print('__metodo_privated')
        return '__metodo_privated'

f = Foo()
# Não deve fazer isso
# print(f._protect)
# print(f._metodo_protected())
# print(f.public)
print(f.metodo_publico())
# Não deve fazer isso para acessar private
print(f._Foo__metodo_privated())