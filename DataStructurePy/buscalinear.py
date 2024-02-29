
#busca linear em lista de alocação sequencial
def busca(lista, elemento):
    for i in range(len(lista)):
        """Retorna o indice do elemento se ele estiver na lista ou none caso o contrário"""
        if lista[i] == elemento:
            return i
    return None


lista = [8, "3", 543, 0, "python", 32]

elemento = "python"

print(busca(lista,elemento))