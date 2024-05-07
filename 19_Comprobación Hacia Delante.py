# Pablo Dario Jimenez Nu*o 21310143

def forward_checking(variables, dominios, restricciones, asignacion):
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
            # Realiza la comprobación hacia delante
            dominios_actualizados = {var: dominios[var][:] for var in variables if var not in nueva_asignacion}
            for var, val in nueva_asignacion.items():
                for vecino in grafo[var]:
                    if vecino in dominios_actualizados:
                        dominios_actualizados[vecino] = [v for v in dominios_actualizados[vecino] if v != val]

            # Verifica si hay algún dominio vacío
            if all(dominios_actualizados[var] for var in dominios_actualizados):
                resultado = forward_checking(variables, dominios_actualizados, restricciones, nueva_asignacion)
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

    # Realizamos la comprobación hacia delante para encontrar una asignación válida
    asignacion_valida = forward_checking(variables, dominios, restricciones, {})

    # Imprimimos la asignación válida encontrada
    if asignacion_valida is not None:
        print("Asignacion valida encontrada:", asignacion_valida)
    else:
        print("No se encontro una asignacion valida.")

