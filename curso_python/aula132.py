# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # ao invés de usar isso usa com underline
        #self.cor_tinta = cor
        # convenção, se ver 1 ou 2 underline significa que 
        # o desenvolvedor não quer que use esse atributo 
        # fora da classe
        self._cor = cor
        self._cor_tampa = None
        
    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
        
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Pink'
print(caneta.cor)
caneta.cor_tampa = 'Azul'
print(caneta.cor_tampa)
