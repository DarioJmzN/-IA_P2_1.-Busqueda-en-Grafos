# Pablo Dario Jimenez Nu*o 21310143

from collections import deque  # Importa la clase deque de la biblioteca collections

# Ejemplo de funcion procesar_nodo
def procesar_nodo(nodo):  # Define una funcion llamada procesar_nodo que toma un nodo como argumento
    print("Nodo procesado:", nodo)  # Imprime un mensaje indicando que el nodo ha sido procesado

# Ejemplo de funcion procesar_lado
def procesar_lado(nodo1, nodo2):  # Define una funcion llamada procesar_lado que toma dos nodos como argumentos
    print("Lado procesado:", nodo1, "-", nodo2)  # Imprime un mensaje indicando que el lado entre los nodos ha sido procesado

def bfs(g, s):  # Define una función llamada bfs que toma un grafo g y un nodo inicial s como argumentos
    nodo_visitado = [False] * len(g)  # Crea una lista de nodos visitados, inicialmente todos son False
    nodo_procesado = [False] * len(g)  # Crea una lista de nodos procesados, inicialmente todos son False
    nodo_padre = [-1] * len(g)  # Crea una lista de nodos padres, inicialmente todos son -1
    cola = deque([s])  # Crea una cola con el nodo inicial s
    nodo_visitado[s] = True  # Marca el nodo inicial como visitado

    while cola:  # Inicia un bucle mientras la cola no este vacia
        v = cola.popleft()  # Obtiene y elimina el primer elemento de la cola
        nodo_procesado[v] = True  # Marca el nodo como procesado
        procesar_nodo(v)  # Llama a la funcion procesar_nodo para el nodo v

        for neighbor in g[v]:  # Itera sobre los vecinos del nodo v en el grafo
            if not nodo_visitado[neighbor]:  # Verifica si el vecino no ha sido visitado
                cola.append(neighbor)  # Agrega el vecino a la cola
                nodo_visitado[neighbor] = True  # Marca el vecino como visitado
                nodo_padre[neighbor] = v  # Establece el nodo v como el padre del vecino

            if not nodo_procesado[neighbor]:  # Verifica si el vecino no ha sido procesado
                procesar_lado(v, neighbor)  # Llama a la funcion procesar_lado para el nodo v y su vecino neighbor

# Ejemplo del grafo 
grafo = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'e', 'd'],
    'd': ['a', 'b', 'e', 'c'],
    'e': ['d', 'b', 'f', 'c'],
    'f': ['e', 'd']
}

# Llama a la funcion BFS con el grafo y el nodo de inicio
print("Recorrido BFS:")
bfs(grafo, 'a')  # Llama a la funcion BFS con el grafo y el nodo de inicio 'a'
