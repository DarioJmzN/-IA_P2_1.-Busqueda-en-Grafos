# Pablo Dario Jimenez Nu*o 21310143

from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])  # Inicializa la cola FIFO con el nodo de inicio
    visited = set([start])  # Conjunto para mantener los nodos visitados

    while queue:
        node = queue.popleft()  # Extrae el primer nodo de la cola
        if node == goal:
            return True  # Retorna True si se encuentra el nodo objetivo

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Agrega los vecinos no visitados a la cola
                visited.add(neighbor)  # Marca los vecinos como visitados

    return False  # Retorna False si no se encuentra el nodo objetivo

# grafo que estamos usando
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'e', 'd'],
    'd': ['a', 'b', 'e', 'c'],
    'e': ['d', 'b', 'f', 'c'],
    'f': ['e', 'd']
}

# Define el nodo de inicio y el nodo objetivo
start_node = 'a'
goal_node = 'f'

# Llama a la función de búsqueda en grafos
if bfs(graph, start_node, goal_node):
    print("Se encontro una ruta entre", start_node, "y", goal_node, "utilizando busqueda en grafos.")
else:
    print("No se encontro una ruta entre", start_node, "y", goal_node, "utilizando busqueda en grafos.")




