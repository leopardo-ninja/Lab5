def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return 0
    return sum(lista_notas) / len(lista_notas)

def encontrar_maximo(lista_notas):
    if len(lista_notas) == 0:
        return 0
    return max(lista_notas)
