# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
    
    def motor(self, motor):
        self._motor = motor
    
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def listar_carro(self):
        print(self._nome, self._motor, self._fabricante)

class Motor:
    def __init__(self, nome):
        self._nome = nome

class Fabricante:
    def __init__(self, nome):
        self._nome = nome

carro1 = Carro('Gol')
motor1 = Motor('AP 1.6')
fabricante1 = Fabricante('Volkswagen')

carro1.motor(motor1._nome)
carro1.fabricante(fabricante1._nome)
carro1.listar_carro()