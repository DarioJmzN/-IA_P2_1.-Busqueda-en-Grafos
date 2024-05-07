# Pablo Dario Jimenez Nu*o 21310143

from collections import deque

def bfs(grafo, inicio, objetivo):
    # Inicializa la cola para la busqueda en anchura
    cola = deque([(inicio, [inicio])])

    # Realiza la busqueda en anchura
    while cola:
        estado, ruta = cola.popleft()
        if estado == objetivo:
            return ruta
        for vecino in grafo.get(estado, []):
            cola.append((vecino, ruta + [vecino]))
    return None

if __name__ == "__main__":
    # Definimos el grafo del laberinto
    laberinto = {
        (0, 0): [(0, 1), (1, 0)],
        (0, 1): [(0, 0), (0, 2)],
        (0, 2): [(0, 1), (1, 2)],
        (1, 0): [(0, 0), (1, 1)],
        (1, 1): [(1, 0), (1, 2)],
        (1, 2): [(0, 2), (1, 1)]
    }

    # Definimos el estado inicial y el objetivo
    estado_inicial = (0, 0)
    estado_objetivo = (1, 2)

    # Realizamos la búsqueda en anchura (aproximación de búsqueda online)
    ruta = bfs(laberinto, estado_inicial, estado_objetivo)

    # Imprimimos la ruta encontrada
    if ruta:
        print("Ruta encontrada:", ruta)
    else:
        print("No se encontro una ruta.")


