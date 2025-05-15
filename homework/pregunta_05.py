"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()

    stats = {}
    for line in data:
        parts = line.strip().split("\t")
        letter = parts[0]
        number = int(parts[1])
        if letter in stats:
            stats[letter].append(number)
        else:
            stats[letter] = [number]

    result = [(letter, max(stats[letter]), min(stats[letter])) for letter in sorted(stats)]
    return result
print(pregunta_05())

"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
