# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
# def soma(a, b, /, x, y):
#     print(a + b + x + y)

# soma(1, 2, 3, y=3)
# soma(a=1, b=2)
# TypeError: soma() got some positional-only 
# arguments passed as keyword arguments: 'a, b'

# def soma(a, b, *, c):
#     print(a + b + c)

# soma(1, 2, c=3)
# soma(1, b=2, c=3)
# soma(1, 2, 3)
# TypeError: soma() takes 2 positional arguments 
# but 3 were given

def soma(a, b, /, *, c):
    print(a + b + c)

soma(1, 2, c=3)

# def soma(*args):
#     print(sum(args))