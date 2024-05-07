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

def a_estrella(graph, start, goal):
    frontier = PriorityQueue()  # Cola de prioridad para nodos frontera
    frontier.put(start, 0)  # Agrega el nodo inicial a la cola de prioridad
    came_from = {}  # Diccionario para almacenar el camino recorrido
    cost_so_far = {}  # Diccionario para almacenar el costo acumulado desde el inicio

    came_from[start] = None  # El nodo inicial no tiene padre
    cost_so_far[start] = 0  # El costo acumulado desde el inicio hasta el inicio es 0

    while not frontier.empty():
        current = frontier.get()  # Obtiene el nodo con el menor costo acumulado + heuristica
        if current == goal:
            break  # Se encontró el objetivo, termina el bucle

        for next_node in graph[current]:
            new_cost = cost_so_far[current] + 1  # Costo del camino desde el inicio hasta next_node
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristico(next_node, goal)  # A* utiliza la suma del costo y la heuristica
                frontier.put(next_node, priority)
                came_from[next_node] = current

    # Reconstruye el camino desde el objetivo al inicio
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

def ao_estrella(graph, start, goal, alpha):
    frontier = PriorityQueue()  # Cola de prioridad para nodos frontera
    frontier.put(start, 0)  # Agrega el nodo inicial a la cola de prioridad
    came_from = {}  # Diccionario para almacenar el camino recorrido
    cost_so_far = {}  # Diccionario para almacenar el costo acumulado desde el inicio

    came_from[start] = None  # El nodo inicial no tiene padre
    cost_so_far[start] = 0  # El costo acumulado desde el inicio hasta el inicio es 0

    while not frontier.empty():
        current = frontier.get()  # Obtiene el nodo con el menor costo acumulado + heuristica
        if current == goal:
            break  # Se encontró el objetivo, termina el bucle

        for next_node in graph[current]:
            new_cost = cost_so_far[current] + 1  # Costo del camino desde el inicio hasta next_node
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = (1 - alpha) * new_cost + alpha * heuristico(next_node, goal)  # AO* con ponderacion alpha
                frontier.put(next_node, priority)
                came_from[next_node] = current

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
    alpha = 0.5  # Factor de ponderacion para AO*

    ruta_a_estrella = a_estrella(graph, nodo_actual, meta)  # Realizamos la busqueda A*
    print("Ruta encontrada con A*:", ruta_a_estrella)

    ruta_ao_estrella = ao_estrella(graph, nodo_actual, meta, alpha)  # Realizamos la busqueda AO*
    print("Ruta encontrada con AO*:", ruta_ao_estrella)

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
