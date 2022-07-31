# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palabra_1 = str(input('Ingrese la primer palabra:'))
palabra_2 = str(input('Ingrese la segunda palabra:'))
palabra_3 = str(input('Ingrese la tercer palabra:'))
consulta = int(input('¿como desea ordenarlas? 1 -alfabéticamente o 2 - por cantidad de letras:'))

# si usuario elige opción 1, ordenar alfabéticamente
if consulta == 1:
    if palabra_1 > palabra_2:
        if palabra_1 > palabra_3:
            orden_3 = palabra_1
            if palabra_2 > palabra_3:
                orden_2 = palabra_2
                orden_1 = palabra_3
            else:
                orden_2 = palabra_3
                orden_1 = palabra_2
    elif palabra_2 > palabra_3:
            orden_3 = palabra_2
            if palabra_1 > palabra_3:
                orden_2 = palabra_1
                orden_1 = palabra_3
            else:
                orden_2 = palabra_3
                orden_1 = palabra_1
    else:
        orden_3 = palabra_3
        if palabra_1 > palabra_2:
            orden_2 = palabra_1
            orden_1 = palabra_2
# si usuario elige opción 2, ordenar por extensión de palabra
elif consulta == 2:
        extension_1 = len(palabra_1)
        extension_2 = len(palabra_2)
        extension_3 = len(palabra_3)
        if extension_1 > extension_2:
            if extension_1 > extension_3:
                orden_3 = palabra_1
                if extension_2 > extension_3:
                    orden_2 = palabra_2
                    orden_1 = palabra_3
                else:
                    orden_2 = palabra_3
                    orden_1 = palabra_2
        elif extension_2 > extension_3:
                orden_3 = palabra_2
                if extension_1 > extension_3:
                    orden_2 = palabra_1
                    orden_1 = palabra_3
                else:
                    orden_2 = palabra_3
                    orden_1 = palabra_1
        else:
            orden_3 = palabra_3
            if extension_1 > extension_2:
                orden_2 = palabra_1
                orden_1 = palabra_2
if consulta == 1:
    print('ordenadas alfabéticamente de Mayor a Menor quedan así: {}, {} y {}'.format(orden_3, orden_2, orden_1))
else:
    print('ordenadas por extensión de Mayor a Menor quedan así: {}, {} y {}'.format(orden_3, orden_2, orden_1))
