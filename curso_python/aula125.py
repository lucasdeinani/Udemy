#Atributos de classe
#ANO_ATUAL = 2024

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100
    
    def get_ano_nascimento(self):
        # return ANO_ATUAL - self.idade
        # return self.ano_atual - self.idade #com o self pode gerar problemas
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())