# Pablo Dario Jimenez Nu*o 21310143

import random

def minimos_conflictos(asignacion, restricciones, max_iteraciones):
    for _ in range(max_iteraciones):
        if restricciones_validas(asignacion, restricciones):
            return asignacion
        
        conflicto_vars = encontrar_conflicto(asignacion, restricciones)
        variable = conflicto_vars[random.randint(0, len(conflicto_vars) - 1)]
        valor = seleccionar_valor(variable, asignacion, restricciones)
        asignacion[variable] = valor
        
    return None

def restricciones_validas(asignacion, restricciones):
    return all(restr(asignacion) for restr in restricciones)

def encontrar_conflicto(asignacion, restricciones):
    conflicto_vars = []
    for restr in restricciones:
        if not restr(asignacion):
            conflicto_vars.extend(restr.variables)
    return set(conflicto_vars)

def seleccionar_valor(variable, asignacion, restricciones):
    valores = list(range(1, len(asignacion) + 1))  # Valores posibles
    random.shuffle(valores)  # Se mezclan los valores para obtener un orden aleatorio
    for valor in valores:
        asignacion[variable] = valor
        if restricciones_validas(asignacion, restricciones):
            return valor
    return None

if __name__ == "__main__":
    # Definimos las variables y las restricciones
    variables = ['a', 'b', 'c', 'd']
    restricciones = [
        lambda asignacion: asignacion['a'] != asignacion['b'],  # Ejemplo de restricción: a != b
        lambda asignacion: asignacion['b'] != asignacion['c'],  # Ejemplo de restricción: b != c
        lambda asignacion: asignacion['c'] != asignacion['d']   # Ejemplo de restricción: c != d
    ]

    # Realizamos la búsqueda local de mínimos conflictos para encontrar una asignación válida
    asignacion_inicial = {var: random.randint(1, len(variables)) for var in variables}
    asignacion_valida = minimos_conflictos(asignacion_inicial, restricciones, max_iteraciones=100)

    # Imprimimos la asignación válida encontrada
    if asignacion_valida is not None:
        print("Asignacion valida encontrada:", asignacion_valida)
    else:
        print("No se encontro una asignacion valida.")


