# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

def value_iteration(transiciones, recompensas, gamma, tol=1e-6):
    # Inicializamos el valor de los estados aleatoriamente
    valores = np.zeros(len(transiciones))

    while True:
        delta = 0
        for estado in range(len(transiciones)):
            v_antiguo = valores[estado]

            # Calculamos el nuevo valor para el estado
            nuevos_valores = []
            for accion in range(len(transiciones[estado])):
                transicion_accion = transiciones[estado][accion]
                valor_accion = sum(transicion_accion[i] * (recompensas[estado][accion][i] + gamma * valores[i]) 
                                   for i in range(len(transicion_accion)))
                nuevos_valores.append(valor_accion)

            # Actualizamos el valor del estado con el máximo valor de las acciones posibles
            valores[estado] = max(nuevos_valores)

            # Actualizamos el delta para verificar la convergencia
            delta = max(delta, abs(v_antiguo - valores[estado]))

        # Verificamos la convergencia
        if delta < tol:
            break

    return valores

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos las transiciones y las recompensas para un problema de 3 estados y 2 acciones
    transiciones = [
        [[0.8, 0.1, 0.1], [0.1, 0.6, 0.3]],
        [[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]],
        [[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]]
    ]
    recompensas = [
        [[1, 0, 0], [0, 1, 0]],
        [[-1, 0, 0], [0, -1, 0]],
        [[0, 0, 0], [0, 0, 0]]
    ]

    # Definimos el factor de descuento gamma
    gamma = 0.9

    # Ejecutamos la iteración de valores
    valores_optimos = value_iteration(transiciones, recompensas, gamma)

    # Imprimimos los valores óptimos para cada estado
    print("Valores óptimos para cada estado:")
    print(valores_optimos)
