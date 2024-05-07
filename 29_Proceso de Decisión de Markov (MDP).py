# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class MDP:
    def __init__(self, transiciones, recompensas, gamma):
        self.transiciones = transiciones  # Matriz de transiciones
        self.recompensas = recompensas    # Matriz de recompensas
        self.gamma = gamma                # Factor de descuento

    def obtener_transicion(self, estado, accion):
        # Devuelve la distribución de probabilidad de transición para una acción dada desde un estado dado
        return self.transiciones[estado][accion]

    def obtener_recompensa(self, estado, accion, prox_estado):
        # Devuelve la recompensa asociada a una transición específica
        return self.recompensas[estado][accion][prox_estado]

    def resolver_mdp(self, politica, tol=1e-6):
        # Inicializamos los valores de los estados
        num_estados = len(self.transiciones)
        valores = np.zeros(num_estados)
        
        while True:
            delta = 0
            for estado in range(num_estados):
                v_antiguo = valores[estado]
                accion = politica[estado]
                
                # Calculamos el nuevo valor para el estado según la política actual
                nuevo_valor = sum(self.obtener_transicion(estado, accion)[prox_estado] * 
                                  (self.obtener_recompensa(estado, accion, prox_estado) + 
                                   self.gamma * valores[prox_estado]) 
                                  for prox_estado in range(num_estados))
                
                # Actualizamos el valor del estado
                valores[estado] = nuevo_valor
                
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

    # Creamos una instancia de MDP
    mdp = MDP(transiciones, recompensas, gamma)

    # Definimos una política aleatoria
    politica = np.random.randint(len(transiciones[0]), size=len(transiciones))

    # Resolvemos el MDP con la política dada
    valores_optimos = mdp.resolver_mdp(politica)

    # Imprimimos los valores óptimos para cada estado
    print("Valores óptimos para cada estado:")
    print(valores_optimos)
