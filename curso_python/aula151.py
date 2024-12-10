# Funções decoradoras e decoradores com classes
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr
# Funciona das duas formas
def adiciona_repr(cls):
    # Só que dai tem que tirar essa função 
    # de dentro já que ela está fora agora
    # def meu_repr(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr
    cls.__repr__ = meu_repr
    return cls


# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    # remove isso por herdou de MyReprMixin
    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    # remove isso por herdou de MyReprMixin
    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)