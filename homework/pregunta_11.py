"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    with open("files/input/data.csv", "r") as f:
    #with open('data.csv', 'r') as f:
        data = f.readlines()

    sum_dict = {}

    for line in data:
        parts = line.strip().split("\t")
        value = int(parts[1])
        letters = parts[3].split(",")
        for letter in letters:
            if letter in sum_dict:
                sum_dict[letter] += value
            else:
                sum_dict[letter] = value

    sorted_sum_dict = dict(sorted(sum_dict.items()))

    return sorted_sum_dict
print(pregunta_11())
"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
