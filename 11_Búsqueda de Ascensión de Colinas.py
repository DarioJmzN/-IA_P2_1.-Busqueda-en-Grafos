# Pablo Dario Jimenez Nu*o 21310143

import random

def heuristico(nodo):
    # Define una funcion heuristica para evaluar la calidad de un nodo
    # En este caso, la heuristica es simplemente el valor asociado al nodo
    # Puedes ajustar esta funcion segun tus necesidades y el problema especifico
    valores = {'a': 3, 'b': 7, 'c': 2, 'd': 5, 'e': 1, 'f': 9}
    return valores[nodo]

def generar_vecinos(nodo):
    # Genera los vecinos de un nodo dado
    # En este caso, los vecinos son simplemente los nodos adyacentes al nodo dado
    # Puedes modificar esta funcion si el problema requiere una definicion diferente de vecinos
    conexiones = {'a': ['b', 'c', 'd'], 'b': ['a', 'c', 'e'], 'c': ['a', 'b', 'e', 'd'],
                  'd': ['a', 'b', 'e', 'c'], 'e': ['d', 'b', 'f', 'c'], 'f': ['e', 'd']}
    return conexiones[nodo]

def ascension_colinas(nodo_inicial):
    # Inicializa el nodo actual con el nodo inicial
    nodo_actual = nodo_inicial

    # Itera hasta alcanzar un maximo local o un numero maximo de iteraciones
    iteraciones = 0
    while True:
        # Evalua la heuristica del nodo actual
        heuristica_actual = heuristico(nodo_actual)

        # Encuentra los vecinos del nodo actual
        vecinos = generar_vecinos(nodo_actual)

        # Encuentra el vecino con la mejor heurística
        mejor_vecino = None
        mejor_heuristica = float('-inf')
        for vecino in vecinos:
            heuristica_vecino = heuristico(vecino)
            if heuristica_vecino > mejor_heuristica:
                mejor_vecino = vecino
                mejor_heuristica = heuristica_vecino

        # Si el vecino con la mejor heuristica tiene una mejor heuristica que el nodo actual,
        # movemos al nodo actual al mejor vecino y continuamos la busqueda
        if mejor_heuristica > heuristica_actual:
            nodo_actual = mejor_vecino
        else:
            # Si no hay vecinos con una mejor heuristica, hemos alcanzado un maximo local
            break

        # Incrementa el contador de iteraciones
        iteraciones += 1

    return nodo_actual

if __name__ == "__main__":
    # Define el nodo inicial para la busqueda de ascension de colinas
    nodo_inicial = 'a'

    # Realiza la busqueda de ascension de colinas
    nodo_maximo_local = ascension_colinas(nodo_inicial)

    # Imprime el resultado
    print("Maximo local encontrado:", nodo_maximo_local)
