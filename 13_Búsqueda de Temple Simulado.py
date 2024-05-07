# Pablo Dario Jimenez Nu*o 21310143

import random
import math

def heuristica(solucion):
    # Define una función heurística para evaluar la calidad de una solución
    # En este caso, la heurística es simplemente la suma de los valores en la solución
    valores = {'a': 3, 'b': 7, 'c': 2, 'd': 5, 'e': 1, 'f': 9}
    return sum(valores[nodo] for nodo in solucion)

def generar_vecino(solucion_actual):
    # Genera un vecino de la solución actual
    # En este ejemplo, el vecino se obtiene intercambiando dos elementos aleatorios en la solución
    vecino = list(solucion_actual)  # Copia la solución actual para modificarla
    i, j = random.sample(range(len(solucion_actual)), 2)  # Selecciona dos índices aleatorios para intercambiar
    vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambia los elementos en los índices seleccionados
    return vecino

def temple_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura):
    # Inicializa la solución actual con la solución inicial
    solucion_actual = list(solucion_inicial)

    # Inicializa la mejor solución encontrada hasta ahora con la solución inicial
    mejor_solucion = list(solucion_actual)

    # Inicializa la temperatura actual con la temperatura inicial
    temperatura_actual = temperatura_inicial

    # Realiza la búsqueda
    for _ in range(iteraciones_por_temperatura):
        # Genera un vecino aleatorio de la solución actual
        vecino = generar_vecino(solucion_actual)

        # Calcula la diferencia de heurística entre la solución actual y el vecino
        diferencia_heuristica = heuristica(vecino) - heuristica(solucion_actual)

        # Si el vecino es mejor que la solución actual, o se acepta probabilísticamente según la temperatura,
        # actualiza la solución actual con el vecino
        if diferencia_heuristica < 0 or random.random() < math.exp(-diferencia_heuristica / temperatura_actual):
            solucion_actual = vecino

        # Si el vecino es mejor que la mejor solución encontrada hasta ahora, actualiza la mejor solución
        if heuristica(vecino) < heuristica(mejor_solucion):
            mejor_solucion = vecino

        # Reduce la temperatura actual
        temperatura_actual *= factor_enfriamiento

    return mejor_solucion, heuristica(mejor_solucion)

if __name__ == "__main__":
    # Define la solución inicial y los parámetros de Temple Simulado
    solucion_inicial = ['a', 'b', 'c', 'd', 'e', 'f']
    temperatura_inicial = 100
    factor_enfriamiento = 0.95
    iteraciones_por_temperatura = 100

    # Realiza la búsqueda de Temple Simulado
    mejor_solucion, mejor_heuristica = temple_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura)

    # Imprime el resultado
    print("Mejor solucion encontrada:", mejor_solucion)
    print("Mejor heuristica encontrada:", mejor_heuristica)
