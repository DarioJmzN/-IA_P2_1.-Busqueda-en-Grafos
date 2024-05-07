# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class AgenteExploracionExplotacion:
    def __init__(self, num_acciones, epsilon=0.1):
        self.num_acciones = num_acciones
        self.epsilon = epsilon

    def seleccionar_accion(self):
        # Selección de la acción utilizando una política epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_acciones)  # Exploración aleatoria
        else:
            return np.argmax(self.Q_values)  # Explotación de la mejor acción según la función de valor

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el número de acciones
    num_acciones = 5

    # Creamos un agente de exploración vs. explotación
    agente = AgenteExploracionExplotacion(num_acciones, epsilon=0.1)

    # Simulamos la selección de acciones
    for _ in range(100):
        accion_seleccionada = agente.seleccionar_accion()
        print("Acción seleccionada:", accion_seleccionada)



