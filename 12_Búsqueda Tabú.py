# Pablo Dario Jimenez Nu*o 21310143

import random

def heuristico(solucion):
    # Define una función heurística para evaluar la calidad de una solución
    # En este caso, la heurística es simplemente la suma de los valores en la solución
    return sum(solucion)

def generar_vecindario(solucion_actual):
    # Genera un vecindario de soluciones a partir de la solución actual
    # En este ejemplo, el vecindario se obtiene intercambiando dos elementos aleatorios en la solución
    vecindario = []
    for _ in range(len(solucion_actual)):
        vecino = list(solucion_actual)  # Copia la solución actual para modificarla
        i, j = random.sample(range(len(solucion_actual)), 2)  # Selecciona dos índices aleatorios para intercambiar
        vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambia los elementos en los índices seleccionados
        vecindario.append(vecino)
    return vecindario

def busqueda_tabu(solucion_inicial, tamano_lista_tabu, iteraciones):
    # Inicializa la solución actual con la solución inicial
    solucion_actual = list(solucion_inicial)
    mejor_solucion = list(solucion_actual)

    # Inicializa la lista tabú como una lista vacía
    lista_tabu = []

    # Inicializa el mejor valor de heurística encontrado hasta ahora
    mejor_heuristica = heuristico(mejor_solucion)

    # Realiza iteraciones de búsqueda
    for _ in range(iteraciones):
        # Genera el vecindario de soluciones a partir de la solución actual
        vecindario = generar_vecindario(solucion_actual)

        # Encuentra la mejor solución en el vecindario que no esté en la lista tabú
        mejor_vecino = None
        mejor_heuristica_vecino = float('-inf')
        for vecino in vecindario:
            heuristica_vecino = heuristico(vecino)
            if heuristica_vecino > mejor_heuristica_vecino and vecino not in lista_tabu:
                mejor_vecino = vecino
                mejor_heuristica_vecino = heuristica_vecino

        # Actualiza la solución actual y la mejor solución si es necesario
        if mejor_vecino:
            solucion_actual = mejor_vecino
            if mejor_heuristica_vecino > mejor_heuristica:
                mejor_solucion = mejor_vecino
                mejor_heuristica = mejor_heuristica_vecino

        # Agrega la solución actual a la lista tabú
        lista_tabu.append(list(solucion_actual))

        # Si la lista tabú excede el tamaño especificado, elimina el elemento más antiguo
        if len(lista_tabu) > tamano_lista_tabu:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_heuristica

if __name__ == "__main__":
    # Define la solución inicial y los parámetros de búsqueda
    solucion_inicial = [1, 2, 3, 4, 5]
    tamano_lista_tabu = 3
    iteraciones = 100

    # Realiza la búsqueda tabú
    mejor_solucion, mejor_heuristica = busqueda_tabu(solucion_inicial, tamano_lista_tabu, iteraciones)

    # Imprime el resultado
    print("Mejor solucion encontrada:", mejor_solucion)
    print("Mejor heuristica encontrada:", mejor_heuristica)
