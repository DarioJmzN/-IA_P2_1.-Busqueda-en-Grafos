# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class POMDP:
    def __init__(self, transiciones, recompensas, observaciones, gamma):
        self.transiciones = transiciones    # Matriz de transiciones
        self.recompensas = recompensas      # Matriz de recompensas
        self.observaciones = observaciones  # Matriz de observaciones
        self.gamma = gamma                  # Factor de descuento

    def obtener_transicion(self, estado, accion):
        # Devuelve la distribución de probabilidad de transición para una acción dada desde un estado dado
        return self.transiciones[estado][accion]

    def obtener_recompensa(self, estado, accion, prox_estado):
        # Devuelve la recompensa asociada a una transición específica
        return self.recompensas[estado][accion][prox_estado]

    def obtener_probabilidad_observacion(self, estado, accion, prox_estado, observacion):
        # Devuelve la probabilidad de observar una determinada observación en un estado dado
        return self.observaciones[estado][accion][prox_estado][observacion]

    def resolver_pomdp(self, politica, tol=1e-6):
        num_estados = len(self.transiciones)
        num_acciones = len(self.transiciones[0])
        num_observaciones = len(self.observaciones[0][0][0])

        valores = np.zeros(num_estados)

        while True:
            delta = 0
            for estado in range(num_estados):
                v_antiguo = valores[estado]
                accion = politica[estado]

                nuevo_valor = 0
                for prox_estado in range(num_estados):
                    transicion_prob = self.obtener_transicion(estado, accion)[prox_estado]
                    recompensa = self.obtener_recompensa(estado, accion, prox_estado)
                    sum_prob_obs = 0
                    for observacion in range(num_observaciones):
                        prob_obs = self.obtener_probabilidad_observacion(estado, accion, prox_estado, observacion)
                        sum_prob_obs += prob_obs * valores[prox_estado]
                    nuevo_valor += transicion_prob * (recompensa + self.gamma * sum_prob_obs)

                valores[estado] = nuevo_valor

                delta = max(delta, abs(v_antiguo - valores[estado]))

            if delta < tol:
                break

        return valores

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos las transiciones, recompensas y observaciones para un problema de 3 estados y 2 acciones
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
    observaciones = [
        [[[0.7, 0.2, 0.1], [0.1, 0.6, 0.3]], [[0.1, 0.2, 0.7], [0.2, 0.7, 0.1]]],
        [[[0.8, 0.1, 0.1], [0.1, 0.8, 0.1]], [[0.6, 0.3, 0.1], [0.1, 0.7, 0.2]]],
        [[[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]], [[0.5, 0.4, 0.1], [0.2, 0.3, 0.5]]]
    ]

    # Definimos el factor de descuento gamma
    gamma = 0.9

    # Creamos una instancia de POMDP
    pomdp = POMDP(transiciones, recompensas, observaciones, gamma)

    # Definimos una política aleatoria
    politica = np.random.randint(len(transiciones[0]), size=len(transiciones))

    # Resolvemos el POMDP con la política dada
    valores_optimos = pomdp.resolver_pomdp(politica)

    # Imprimimos los valores óptimos para cada estado
    print("Valores óptimos para cada estado:")
    print(valores_optimos)
