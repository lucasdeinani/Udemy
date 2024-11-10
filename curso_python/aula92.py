# Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')    

def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen #gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')

g1 = gen2(gen1()) #gen
g2 = gen2(gen3()) #gen
g3 = gen2() #gen
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)