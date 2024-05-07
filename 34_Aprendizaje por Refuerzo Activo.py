# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class QLearning:
    def __init__(self, num_estados, num_acciones, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Tasa de exploración
        self.Q = np.zeros((num_estados, num_acciones))  # Función de valor acción-estado

    def seleccionar_accion(self, estado):
        # Selección de la acción utilizando una política epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_acciones)
        else:
            return np.argmax(self.Q[estado])

    def actualizar_q_values(self, estado_actual, accion, recompensa, estado_siguiente):
        # Actualización de la función de valor acción-estado utilizando el algoritmo Q-Learning
        mejor_siguiente_valor = np.max(self.Q[estado_siguiente])
        delta = recompensa + self.gamma * mejor_siguiente_valor - self.Q[estado_actual][accion]
        self.Q[estado_actual][accion] += self.alpha * delta

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el número de estados y acciones
    num_estados = 5
    num_acciones = 2

    # Creamos un agente Q-Learning
    agente_q_learning = QLearning(num_estados, num_acciones)

    # Simulamos episodios de aprendizaje
    for _ in range(1000):
        # Simulamos un episodio de ejemplo
        estado_actual = 0
        for _ in range(10):
            accion = agente_q_learning.seleccionar_accion(estado_actual)
            recompensa = np.random.randint(0, 10)  # Recompensa aleatoria
            estado_siguiente = np.random.randint(0, num_estados)  # Estado siguiente aleatorio
            agente_q_learning.actualizar_q_values(estado_actual, accion, recompensa, estado_siguiente)
            estado_actual = estado_siguiente

    # Imprimimos la función de valor acción-estado aprendida por el agente
    print("Función de Valor Acción-Estado (Q-values):")
    print(agente_q_learning.Q)




