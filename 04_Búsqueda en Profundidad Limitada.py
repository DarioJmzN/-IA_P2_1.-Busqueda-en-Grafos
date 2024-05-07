# Pablo Dario Jimenez Nu*o 21310143

def dls(graph, node, goal, depth_limit, depth=0, visited=None):
    if visited is None:
        visited = set()  # Conjunto para mantener los nodos visitados

    if node == goal:
        return True  # Retorna True si el nodo actual es el objetivo
    
    if depth >= depth_limit:
        return False  # Retorna False si se alcanza el limite de profundidad

    visited.add(node)  # Marca el nodo actual como visitado
    print(node, end=" ")  # Imprime el nodo actual

    for neighbor in graph[node]:  # Itera sobre los vecinos del nodo actual
        if neighbor not in visited:  # Verifica si el vecino no ha sido visitado
            if dls(graph, neighbor, goal, depth_limit, depth + 1, visited):  # Llama recursivamente a la funcion dls con el vecino como nodo actual y aumenta la profundidad
                return True  # Si se encuentra el objetivo en el subarbol, retorna True

    return False  # Si no se encuentra el objetivo en el subarbol, retorna False

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
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
depth_limit = 3  # Define el limite de profundidad

# Llama a la funcion DLS con el grafo, el nodo de inicio, el nodo objetivo y el limite de profundidad
print("Recorrido DLS:")
if dls(graph, start_node, goal_node, depth_limit):
    print("\nSe encontro una ruta desde", start_node, "hasta", goal_node, "dentro del limite de profundidad.")
else:
    print("\nNo se encontro una ruta desde", start_node, "hasta", goal_node, "dentro del limite de profundidad.")

