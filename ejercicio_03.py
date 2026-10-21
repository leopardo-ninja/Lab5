"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""
def dias_del_mes(mes):
    dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias[mes]

def dia_del_anio(mes, dia):
    total_dias = 0
    for m in range(1, mes):
        total_dias += dias_del_mes(m)
    total_dias += dia
    return total_dias

print("--- CALCULADORA DE DÍAS DEL AÑO ---")
while True:
    mes_actual = int(input("Ingrese el número del mes actual (1-12): "))
    if 1 <= mes_actual <= 12:
        break
    print("Error: El mes debe estar entre 1 y 12. Intente de nuevo.")

while True:
    limite_dias = dias_del_mes(mes_actual)
    dia_actual = int(input(f"Ingrese el día actual (1 a {limite_dias}): "))
    if 1 <= dia_actual <= limite_dias:
        break
    print(f"Error: Para este mes el día debe estar entre 1 y {limite_dias}. Intente de nuevo.")

resultado_final = dia_del_anio(mes_actual, dia_actual)

print(f"\n¡Listo! El día {dia_actual} del mes {mes_actual} es el **día número {resultado_final}** del año.")
