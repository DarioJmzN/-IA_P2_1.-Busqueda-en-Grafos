# Pablo Dario Jimenez Nu*o 21310143

import math  # Importamos la libreria math.

def heuristico(nodo_actual, meta):
    # Declaramos nuestras coordenadas de nuestro grafo en base a la imagen
    coordenadas = {        #cordenadas de nuestro grafo  
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
    nodo_actual = 'a'  # Definimos el nodo actual y el nodo meta.
    meta = 'f'

    valor_h = heuristico(nodo_actual, meta)  # Calculamos la heuristica para el nodo actual.
    print("El valor heuristico para el nodo actual:", valor_h)
