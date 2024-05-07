# Pablo Dario Jimenez Nu*o 21310143

def backtracking(variables, dominios, restricciones, asignacion):
    # Verifica si se ha asignado un valor a todas las variables
    if len(asignacion) == len(variables):
        return asignacion

    # Selecciona la próxima variable sin asignar
    variable = next(var for var in variables if var not in asignacion)

    # Intenta asignar un valor a la variable
    for valor in dominios[variable]:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[variable] = valor

        # Verifica si la asignación es válida para todas las restricciones
        restricciones_cumplidas = all(restr(nueva_asignacion) for restr in restricciones)

        if restricciones_cumplidas:
            resultado = backtracking(variables, dominios, restricciones, nueva_asignacion)
            if resultado is not None:
                return resultado

    return None

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
    restricciones = [
        lambda asignacion: asignacion[var1] != asignacion[var2] for var1 in grafo for var2 in grafo[var1]  # var1 != var2
    ]

    # Realizamos la búsqueda de vuelta atrás para encontrar una asignación válida
    asignacion_valida = backtracking(variables, dominios, restricciones, {})

    # Imprimimos la asignación válida encontrada
    if asignacion_valida is not None:
        print("Asignacion valida encontrada:", asignacion_valida)
    else:
        print("No se encontro una asignacion valida.")

