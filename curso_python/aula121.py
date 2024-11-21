# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamento no código
class Carro:
    def __init__(self, nome):
        # self.nome = 'Fusca' # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
fusca.acelerar()