"""
Introdução ao desenpacotamento
"""
# nome1, nome2 = ['Maria', 'Helena', 'Luiz'] # Gera erro
# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz'] # Gera erro
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# nome, *resto = ['Maria', 'Helena', 'Luiz']
# nome, *_ = ['Maria', 'Helena', 'Luiz'] # Melhor utilizar o underline para dizer que não vai pegar
_, nome, *_ = ['Maria', 'Helena', 'Luiz'] # Melhor utilizar o underline para dizer que não vai pegar
_, nome, *_ = ['Maria', 'Helena', 'Luiz'] # Melhor utilizar o underline para dizer que não vai pegar

print(nome, type(nome))