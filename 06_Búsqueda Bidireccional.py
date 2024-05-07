# Pablo Dario Jimenez Nu*o 21310143

def bidirectional_search(graph, start, goal):
    forward_queue = [start]  # Cola para la busqueda en la direccion hacia adelante
    backward_queue = [goal]  # Cola para la busqueda en la direccion hacia atras
    forward_visited = set([start])  # Conjunto para mantener los nodos visitados en la direccion hacia adelante
    backward_visited = set([goal])  # Conjunto para mantener los nodos visitados en la direccion hacia atras

    while forward_queue and backward_queue:
        # Busqueda en la direccion hacia adelante
        current_forward = forward_queue.pop(0)
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited.add(neighbor)
            if neighbor in backward_visited:
                return True  # Se encontro una conexion entre las dos busquedas

        # Busqueda en la direccion hacia atras
        current_backward = backward_queue.pop(0)
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited.add(neighbor)
            if neighbor in forward_visited:
                return True  # Se encontro una conexion entre las dos busquedas

    return False  # No se encontro una conexion entre las dos busquedas

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

# Llama a la funcion de busqueda bidireccional
if bidirectional_search(graph, start_node, goal_node):
    print("Se encontro una ruta entre", start_node, "y", goal_node, "utilizando busqueda bidireccional.")
else:
    print("No se encontro una ruta entre", start_node, "y", goal_node, "utilizando busqueda bidireccional.")



