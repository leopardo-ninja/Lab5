"""
EJERCICIO 02: Validación de contraseña segura

Implementa una función que reciba una contraseña y verifique: 
    1. Que tenga al menos 8 caracteres de longitud.
    2. Que contenga al menos un número (puedes usar un bucle o una verificación con dígitos).
    3. Que contenga al menos una letra mayúscula.

La función debe retornar True si cumple todas las condiciones, y False en caso contrario. 
(Ayuda: puedes crear funciones auxiliares pequeñas para cada validación, fomentando la modularidad de tu programa).

Ejemplos de casos de prueba:
    - es_contrasena_segura("Python123") -> True
    - es_contrasena_segura("clave") -> False
    - es_contrasena_segura("12345678") -> False
"""
def es_contrasena_segura(contrasena):
    if len(contrasena) < 8:
        return False
    
    tiene_numero = False
    tiene_mayuscula = False
    
    for caracter in contrasena:
        if caracter in "0123456789":
            tiene_numero = True
            
        if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tiene_mayuscula = True

        if caracter in "abcdefghijklmnopqrstuvwxyz":
            tiene_minuscula = True
 
            
    return tiene_numero and tiene_mayuscula and tiene_minuscula

print(es_contrasena_segura("Python123")) 
print(es_contrasena_segura("clave"))      
print(es_contrasena_segura("12345678"))   
