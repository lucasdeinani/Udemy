# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados 
# Uma classe pode gerar várias instâncias. 
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        # self.nome = 'Fusca' # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
fusca.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# fusca.acelerar()