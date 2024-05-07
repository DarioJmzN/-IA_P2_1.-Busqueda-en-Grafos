# Pablo Dario Jimenez Nu*o 21310143

import heapq

def ucs(graph, start, goal):
    queue = [(0, start)]  # Inicializa la cola de prioridad con el nodo inicial y su costo acumulado
    visited = set()  # Conjunto para mantener los nodos visitados

    while queue:
        cost, node = heapq.heappop(queue)  # Extrae el nodo con el menor costo acumulado
        if node == goal:  # Verifica si el nodo actual es el objetivo
            return cost  # Retorna el costo acumulado hasta el nodo objetivo

        if node not in visited:  # Verifica si el nodo no ha sido visitado
            visited.add(node)  # Marca el nodo como visitado
            for neighbor, neighbor_cost in graph[node].items():  # Itera sobre los vecinos del nodo
                if neighbor not in visited:  # Verifica si el vecino no ha sido visitado
                    next_cost = cost + neighbor_cost  # Calcula el costo acumulado hasta el vecino
                    heapq.heappush(queue, (next_cost, neighbor))  # Agrega el vecino a la cola de prioridad con su costo acumulado

    return float('inf')  # Retorna infinito si no se puede alcanzar el nodo objetivo

# Ejemplo de grafo representado como un diccionario de diccionarios de adyacencia con costos
graph = {
    'a': {'b': 1, 'c': 2, 'd': 3},
    'b': {'a': 1, 'c': 2, 'e': 4},
    'c': {'a': 2, 'b': 2, 'e': 4, 'd': 3},
    'd': {'a': 3, 'b': 3, 'e': 4, 'c': 3},
    'e': {'d': 3, 'b': 4, 'f': 5, 'c': 4},
    'f': {'e': 5, 'd': 5}
}

# Define el nodo de inicio y el nodo objetivo
start_node = 'a'
goal_node = 'f'

# Llama a la función UCS con el grafo, el nodo de inicio y el nodo objetivo
cost = ucs(graph, start_node, goal_node)

# Imprime el costo mínimo encontrado
if cost != float('inf'):
    print("El costo mínimo desde", start_node, "hasta", goal_node, "es:", cost)
else:
    print("No se pudo encontrar una ruta desde", start_node, "hasta", goal_node)
