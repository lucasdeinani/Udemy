# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # print('Antes de criar a inst')
        instancia = super().__new__(cls)
        # print('Depois')
        # instancia.x = 213
        # return object.__new__(A)
        # Melhor utilizar esta forma abaixo
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return f'{type(self).__name__}()'

a = A(123)
print(a)
print(a.x)
# por baixo dos panos o Python faz isso:
# a = object.__new__(A)
# a.__init__()
# print(a)
