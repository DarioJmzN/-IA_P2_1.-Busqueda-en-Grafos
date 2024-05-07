# Pablo Dario Jimenez Nu*o 21310143

import random

def generar_poblacion(tamano_poblacion, grafo):
    # Genera una población inicial de soluciones aleatorias
    poblacion = []
    for _ in range(tamano_poblacion):
        solucion = list(grafo.keys())  # Inicializa la solución como una lista de nodos del grafo
        random.shuffle(solucion)  # Mezcla aleatoriamente los nodos para generar una solución aleatoria
        poblacion.append(solucion)
    return poblacion

def calcular_fitness(solucion, grafo):
    # Calcula la calidad (fitness) de una solución en función de la suma de los valores de los nodos en la solución
    return sum(grafo[nodo] for nodo in solucion)

def seleccion(poblacion, grafo, tamano_torneo):
    # Realiza una selección de padres mediante un torneo
    padres_seleccionados = []
    for _ in range(len(poblacion)):
        competidores = random.sample(poblacion, tamano_torneo)  # Selecciona aleatoriamente un subconjunto de la población
        mejor_competidor = max(competidores, key=lambda x: calcular_fitness(x, grafo))  # Selecciona el mejor competidor
        padres_seleccionados.append(mejor_competidor)
    return padres_seleccionados

def cruzar(padres_seleccionados):
    # Realiza el cruce de los padres seleccionados para producir hijos
    hijos = []
    for i in range(0, len(padres_seleccionados), 2):
        padre1 = padres_seleccionados[i]
        padre2 = padres_seleccionados[i + 1]
        punto_cruce = random.randint(1, len(padre1) - 1)  # Selecciona un punto de cruce aleatorio
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        hijos.extend([hijo1, hijo2])
    return hijos

def mutar(hijos, probabilidad_mutacion):
    # Realiza la mutación de los hijos con una probabilidad determinada
    for hijo in hijos:
        if random.random() < probabilidad_mutacion:
            # Intercambia dos nodos aleatorios en el hijo para realizar la mutación
            i, j = random.sample(range(len(hijo)), 2)
            hijo[i], hijo[j] = hijo[j], hijo[i]
    return hijos

def algoritmo_genetico(grafo, tamano_poblacion, tamano_torneo, probabilidad_mutacion, generaciones):
    # Genera la población inicial
    poblacion = generar_poblacion(tamano_poblacion, grafo)

    # Realiza el bucle de generaciones
    for _ in range(generaciones):
        # Realiza la selección de padres
        padres_seleccionados = seleccion(poblacion, grafo, tamano_torneo)

        # Realiza el cruce de los padres seleccionados
        hijos = cruzar(padres_seleccionados)

        # Realiza la mutación de los hijos
        hijos_mutados = mutar(hijos, probabilidad_mutacion)

        # Reemplaza la población actual con los hijos mutados
        poblacion = hijos_mutados

    # Encuentra la mejor solución en la última población
    mejor_solucion = max(poblacion, key=lambda x: calcular_fitness(x, grafo))
    mejor_fitness = calcular_fitness(mejor_solucion, grafo)

    return mejor_solucion, mejor_fitness

if __name__ == "__main__":
    # Define los parámetros del algoritmo genético
    grafo = {'a': 3, 'b': 7, 'c': 2, 'd': 5, 'e': 1, 'f': 9}
    tamano_poblacion = 50
    tamano_torneo = 5
    probabilidad_mutacion = 0.1
    generaciones = 100

    # Ejecuta el algoritmo genético
    mejor_solucion, mejor_fitness = algoritmo_genetico(grafo, tamano_poblacion, tamano_torneo, probabilidad_mutacion, generaciones)

    # Imprime el resultado
    print("Mejor solucion encontrada:", mejor_solucion)
    print("Mejor fitness encontrado:", mejor_fitness)

