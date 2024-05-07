# Pablo Dario Jimenez Nu*o 21310143

from queue import PriorityQueue

def heuristico(nodo_actual, meta):
    # Declaramos nuestras coordenadas de nuestro grafo en base a la imagen
    coordenadas = {         
        'a': (0, 0), 
        'b': (1, 3), 
        'c': (2, 2), 
        'd': (3, 0),
        'e': (4, 3), 
        'f': (5, 1), 
    }

    # Obtenemos las coordenadas del nodo actual y del nodo meta.
    x1, y1 = coordenadas[nodo_actual.lower()]  
    x2, y2 = coordenadas[meta.lower()]        
    
    # Calculamos la distancia entre las coordenadas.
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Distancia euclidiana.
    # distancia = abs(x2 - x1) + abs(y2 - y1)           # Distancia Manhattan.
    
    return distancia

def voraz_primero_el_mejor(graph, start, goal):
    frontier = PriorityQueue()  # Cola de prioridad para nodos frontera
    frontier.put(start, 0)  # Agrega el nodo inicial a la cola de prioridad
    came_from = {}  # Diccionario para almacenar el camino recorrido
    came_from[start] = None  # El nodo inicial no tiene padre

    while not frontier.empty():
        current = frontier.get()  # Obtiene el nodo con la menor heuristica
        if current == goal:
            break  # Se encontró el objetivo, termina el bucle

        for next_node in graph[current]:
            if next_node not in came_from:
                priority = heuristico(next_node, goal)  # Calcula la heuristica del siguiente nodo
                frontier.put(next_node, priority)  # Agrega el siguiente nodo a la cola de prioridad
                came_from[next_node] = current  # Registra el padre del siguiente nodo en el camino recorrido

    # Reconstruye el camino desde el objetivo al inicio
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

# Grafo que estamos usando
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'e', 'd'],
    'd': ['a', 'b', 'e', 'c'],
    'e': ['d', 'b', 'f', 'c'],
    'f': ['e', 'd']
}

if __name__ == "__main__":
    nodo_actual = 'a'  # Definimos el nodo actual y el nodo objetivo
    meta = 'f'

    ruta = voraz_primero_el_mejor(graph, nodo_actual, meta)  # Realizamos la busqueda voraz primero el mejor
    print("Ruta encontrada:", ruta)
