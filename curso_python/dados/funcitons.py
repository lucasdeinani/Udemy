def ordena(lista, ordena, reverso=False):
    return sorted(lista, key=lambda item: item[ordena], reverse=reverso)