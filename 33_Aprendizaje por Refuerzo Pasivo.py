# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class AgenteMonteCarlo:
    def __init__(self, num_estados, num_acciones, epsilon=0.1, gamma=1.0):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.epsilon = epsilon  # Tasa de exploración
        self.gamma = gamma  # Factor de descuento
        self.Q = np.zeros((num_estados, num_acciones))  # Función de valor acción-estado
        self.N = np.zeros((num_estados, num_acciones))  # Número de visitas por acción-estado

    def seleccionar_accion(self, estado):
        # Selección de la acción usando una política epsilon-greedy
        if np.random.random() < self.epsilon:
            return np.random.choice(self.num_acciones)
        else:
            return np.argmax(self.Q[estado])

    def actualizar_q_values(self, episodio):
        # Actualización de la función de valor acción-estado usando el algoritmo de Monte Carlo
        estados_visitados = set()
        for t, (estado, accion, recompensa) in enumerate(episodio):
            if estado not in estados_visitados:
                estados_visitados.add(estado)
                G = sum(self.gamma ** i * paso[2] for i, paso in enumerate(episodio[t:]))
                self.N[estado][accion] += 1
                alpha = 1 / self.N[estado][accion]  # Tasa de aprendizaje adaptativa
                self.Q[estado][accion] += alpha * (G - self.Q[estado][accion])

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el número de estados y acciones
    num_estados = 5
    num_acciones = 2

    # Creamos un agente de Monte Carlo
    agente_mc = AgenteMonteCarlo(num_estados, num_acciones)

    # Simulamos episodios de aprendizaje
    for _ in range(1000):
        # Creamos un episodio
        episodio = [(0, 0, 1), (1, 1, 1), (2, 0, 1), (3, 1, 1), (4, 0, 1)]  # Ejemplo de un episodio

        # Actualizamos la función de valor acción-estado del agente
        agente_mc.actualizar_q_values(episodio)

    # Imprimimos la función de valor acción-estado aprendida por el agente
    print("Función de Valor Acción-Estado (Q-values):")
    print(agente_mc.Q)

