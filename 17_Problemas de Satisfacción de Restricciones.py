# Pablo Dario Jimenez Nu*o 21310143

def dfs(variables, dominios, restricciones, asignacion):
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
            resultado = dfs(variables, dominios, restricciones, nueva_asignacion)
            if resultado is not None:
                return resultado

    return None

if __name__ == "__main__":
    # Definimos las variables, dominios y restricciones
    variables = ['a', 'b', 'c', 'd']
    dominios = {
        'a': [1, 2],
        'b': [3, 4],
        'c': [2, 3],
        'd': [1, 4]
    }
    restricciones = [
        lambda asignacion: asignacion['a'] != asignacion['b'],  # Ejemplo de restricción: a != b
        lambda asignacion: asignacion['b'] != asignacion['c'],  # Ejemplo de restricción: b != c
        lambda asignacion: asignacion['c'] != asignacion['d']   # Ejemplo de restricción: c != d
    ]

    # Realizamos la búsqueda en profundidad para encontrar una asignación válida
    asignacion_valida = dfs(variables, dominios, restricciones, {})

    # Imprimimos la asignación válida encontrada
    if asignacion_valida is not None:
        print("Asignacion valida encontrada:", asignacion_valida)
    else:
        print("No se encontro una asignacion valida.")

