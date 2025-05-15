"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv", "r") as f:
     #with open('data.csv','r') as f:
        data = f.readlines()

        result = []
        for line in data:
            parts = line.strip().split("\t")
            letter = parts[0]
            col4_count = len(parts[3].split(","))
            col5_count = len(parts[4].split(","))
            result.append((letter, col4_count, col5_count))

        return result
print(pregunta_10())
"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
