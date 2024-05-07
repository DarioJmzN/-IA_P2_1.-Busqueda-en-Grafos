# Pablo Dario Jimenez Nu*o 21310143

def conflict_directed_backjumping(variables, dominios, restricciones):
    asignacion = {}
    historial_conflictos = {}

    while len(asignacion) < len(variables):
        variable = seleccionar_variable(variables, asignacion, historial_conflictos)

        if variable is None:
            return None  # No se pudo encontrar una asignación válida

        valor = seleccionar_valor(variable, dominios[variable])

        asignacion[variable] = valor

        if restricciones_validas(asignacion, restricciones):
            continue

        conflicto, nivel_conflicto = encontrar_conflicto(asignacion, restricciones)

        if conflicto is None:
            return None  # No se pudo encontrar una asignación válida

        historial_conflictos[conflicto] = max(historial_conflictos.get(conflicto, 0), nivel_conflicto)

        asignacion = {var: asignacion[var] for var in asignacion if historial_conflictos.get(var, 0) < nivel_conflicto}

    return asignacion

def seleccionar_variable(variables, asignacion, historial_conflictos):
    for var in variables:
        if var not in asignacion and var not in historial_conflictos:
            return var
    return None

def seleccionar_valor(variable, dominio):
    return dominio[0]

def restricciones_validas(asignacion, restricciones):
    return all(restr(asignacion) for restr in restricciones)

def encontrar_conflicto(asignacion, restricciones):
    for nivel_conflicto, restr in enumerate(restricciones, start=1):
        if not restr(asignacion):
            return next(var for var in restr.variables if var in asignacion), nivel_conflicto
    return None, None

if __name__ == "__main__":
    # Definimos las variables, dominios y restricciones
    variables = ['a', 'b', 'c', 'd']
    dominios = {
        'a': [1, 2],
        'b': [1, 2],
        'c': [1, 2],
        'd': [1, 2]
    }
    restricciones = [
        lambda asignacion: asignacion['a'] != asignacion['b'],  # Ejemplo de restricción: a != b
        lambda asignacion: asignacion['b'] != asignacion['c'],  # Ejemplo de restricción: b != c
        lambda asignacion: asignacion['c'] != asignacion['d']   # Ejemplo de restricción: c != d
    ]

    # Realizamos el salto atrás dirigido por conflictos para encontrar una asignación válida
    asignacion_valida = conflict_directed_backjumping(variables, dominios, restricciones)

    # Imprimimos la asignación válida encontrada
    if asignacion_valida is not None:
        print("Asignacion valida encontrada:", asignacion_valida)
    else:
        print("No se encontro una asignacion valida.")


