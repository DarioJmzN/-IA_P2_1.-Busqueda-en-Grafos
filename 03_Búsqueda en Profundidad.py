# Pablo Dario Jimenez Nu*o 21310143

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Conjunto para mantener los nodos visitados
    visited.add(start)  # Marca el nodo actual como visitado
    print(start, end=" ")  # Imprime el nodo actual

    for neighbor in graph[start]:  # Itera sobre los vecinos del nodo actual
        if neighbor not in visited:  # Verifica si el vecino no ha sido visitado
            dfs(graph, neighbor, visited)  # Llama recursivamente a la funcion dfs con el vecino como nodo actual

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'e', 'd'],
    'd': ['a', 'b', 'e', 'c'],
    'e': ['d', 'b', 'f', 'c'],
    'f': ['e', 'd']
}

# Define el nodo de inicio
start_node = 'a'

# Llama a la funcion DFS con el grafo y el nodo de inicio
print("Recorrido para la Busqueda en Profundidad:")
dfs(graph, start_node)
