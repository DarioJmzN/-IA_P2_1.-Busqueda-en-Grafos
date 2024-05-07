# Pablo Dario Jimenez Nu*o 21310143

from collections import deque

def ac3(grafo, variables, dominios, restricciones):
    cola_arcs = deque([(X, Y) for X in grafo for Y in grafo[X]])

    while cola_arcs:
        (X, Y) = cola_arcs.popleft()

        if remover_inconsistentes(X, Y, grafo, dominios, restricciones):
            if not dominios[X]:
                return False  # Se encontró un dominio vacío, no hay solución

            for Z in grafo[X]:
                if Z != Y:
                    cola_arcs.append((Z, X))
    return True  # Todos los arcos fueron consistentes, hay solución

def remover_inconsistentes(X, Y, grafo, dominios, restricciones):
    removido = False
    dominios_actualizados = dominios[X][:]

    for x_valor in dominios[X]:
        existe_y_valor_valido = any(restr(X, x_valor, Y, y_valor) for y_valor in dominios[Y])
        if not existe_y_valor_valido:
            dominios_actualizados.remove(x_valor)
            removido = True

    dominios[X] = dominios_actualizados
    return removido

if __name__ == "__main__":
    # Definimos el grafo y sus variables
    grafo = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'e'],
        'c': ['a', 'b', 'e', 'd'],
        'd': ['a', 'b', 'e', 'c'],
        'e': ['d', 'b', 'f', 'c'],
        'f': ['e', 'd']
    }
    variables = list(grafo.keys())

    # Definimos los dominios de las variables
    dominios = {var: list(range(1, len(variables) + 1)) for var in variables}

    # Definimos las restricciones
    restricciones = lambda X, x, Y, y: x != y  # Restricción de que dos variables no pueden tener el mismo valor

    # Realizamos la propagación de restricciones
    solucion = ac3(grafo, variables, dominios, restricciones)

    # Imprimimos la solución
    if solucion:
        print("Se encontro una solucion:")
        for variable, valor in dominios.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontro una solucion.")

