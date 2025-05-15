"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
   conteo = {}
   with open('files/input/data.csv', 'r') as data:
       for line in data:
           letra = line.strip().split('\t')[0]
           conteo[letra] = conteo.get(letra, 0) + 1

   return sorted(conteo.items())

print(pregunta_02())
"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
