from paquete_academico.operaciones import calcular_promedio, encontrar_maximo

def generar_resumen(lista_notas):
    promedio = calcular_promedio(lista_notas)
    maximo = encontrar_maximo(lista_notas)
    
    print("===== REPORTE ACADÉMICO =====")
    print(f"Notas evaluadas: {lista_notas}")
    print(f"Promedio general: {promedio}")
    print(f"Nota más alta: {maximo}")
    print("=============================")