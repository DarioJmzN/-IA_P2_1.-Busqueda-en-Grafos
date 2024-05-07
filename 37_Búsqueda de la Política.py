# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class AgenteBusquedaPolitica:
    def __init__(self, num_estados, num_acciones):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.Q_values = np.zeros((num_estados, num_acciones))  # Función de valor acción-estado

    def seleccionar_accion(self, estado):
        # Selección de la acción basada en la política de mejor acción según la función de valor
        return np.argmax(self.Q_values[estado])

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el número de estados y acciones
    num_estados = 5
    num_acciones = 3

    # Creamos un agente de búsqueda de política
    agente = AgenteBusquedaPolitica(num_estados, num_acciones)

    # Simulamos la selección de acciones para diferentes estados
    for estado in range(num_estados):
        accion_seleccionada = agente.seleccionar_accion(estado)
        print("Acción seleccionada para el estado", estado, ":", accion_seleccionada)



