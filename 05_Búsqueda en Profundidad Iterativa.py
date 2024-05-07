# Pablo Dario Jimenez Nu*o 21310143

def dls(graph, start, goal, max_depth):
    for depth_limit in range(max_depth + 1):  # Itera sobre los limites de profundidad desde 0 hasta max_depth
        visited = set()  # Conjunto para mantener los nodos visitados
        if dls_recursive(graph, start, goal, depth_limit, visited):  # Llama a la busqueda en profundidad limitada recursiva
            return True  # Si encuentra el objetivo, retorna True
    return False  # Si no encuentra el objetivo para ningun limite de profundidad, retorna False

def dls_recursive(graph, node, goal, depth_limit, visited):
    if node == goal:
        return True  # Retorna True si el nodo actual es el objetivo

    if depth_limit == 0:
        return False  # Retorna False si se alcanza el limite de profundidad

    visited.add(node)  # Marca el nodo actual como visitado

    for neighbor in graph[node]:  # Itera sobre los vecinos del nodo actual
        if neighbor not in visited:  # Verifica si el vecino no ha sido visitado
            if dls_recursive(graph, neighbor, goal, depth_limit - 1, visited):  # Llama recursivamente a la busqueda en profundidad limitada
                return True  # Si encuentra el objetivo en el subarbol, retorna True

    return False  # Si no encuentra el objetivo en el subarbol, retorna False

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
max_depth = 5  # Define el limite maximo de profundidad

# Llama a la funcion IDDFS con el grafo, el nodo de inicio, el nodo objetivo y el limite maximo de profundidad
print("Recorrido IDDFS:")
if dls(graph, start_node, goal_node, max_depth):
    print("\nSe encontro una ruta desde", start_node, "hasta", goal_node, "dentro del limite maximo de profundidad.")
else:
    print("\nNo se encontro una ruta desde", start_node, "hasta", goal_node, "dentro del limite maximo de profundidad.")


