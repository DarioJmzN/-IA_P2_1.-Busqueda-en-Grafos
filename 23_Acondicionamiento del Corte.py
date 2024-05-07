# Pablo Dario Jimenez Nu*o 21310143

def cutset_conditioning(modelo, cutset, evidencia):
    # Elimina las variables condicionadas del modelo
    for variable in cutset:
        del modelo[variable]

    # Actualiza las probabilidades condicionales del modelo según la evidencia
    for variable, valor in evidencia.items():
        for var, prob in modelo.items():
            if variable in prob:
                modelo[var] = {k: v for k, v in prob.items() if k[variable] == valor}

    # Calcula las probabilidades marginales actualizadas
    marginales = {}
    for variable in modelo.keys():
        marginales[variable] = {k: v for k, v in modelo[variable].items()}

    return marginales

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un modelo probabilístico como un diccionario de diccionarios
    modelo = {
        'A': {(0,): 0.6, (1,): 0.4},
        'B': {(0,): 0.7, (1,): 0.3},
        'C': {(0, 0): 0.8, (0, 1): 0.2, (1, 0): 0.3, (1, 1): 0.7},
        'D': {(0, 0): 0.5, (0, 1): 0.5, (1, 0): 0.6, (1, 1): 0.4}
    }

    # Definimos un conjunto de corte (cutset)
    cutset = ['C', 'D']

    # Definimos la evidencia
    evidencia = {'A': 0, 'B': 1}

    # Aplicamos el acondicionamiento del corte al modelo con la evidencia dada
    marginales_actualizadas = cutset_conditioning(modelo, cutset, evidencia)

    # Imprimimos las probabilidades marginales actualizadas
    print("Probabilidades marginales actualizadas:")
    for variable, prob in marginales_actualizadas.items():
        print(f"{variable}: {prob}")

