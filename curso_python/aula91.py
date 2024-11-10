# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Mais uma...')
#     yield 3 # Pausar
#     print('Vou terminar')
#     return 'ACABOU' #StopIteration: ACABOU

def generator(n=0, maximum=10):
    while True:
        yield n
        
        n += 1

        if n >= maximum:
            return

#gen = generator(n=0)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

gen = generator()
gen = generator(n=5, maximum=8)
gen = generator(maximum=3)
for n in gen:
    print(n)


def generator_teste(numeros=0):
    for numero in range(numeros):
        yield numero

gen = generator_teste(10)
for n in gen:
    print(n)