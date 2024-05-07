# Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import nashpy as nash

# Definición de las matrices de pagos del juego
jugador1 = np.array([[3, 2], [0, 1]])
jugador2 = np.array([[3, 0], [2, 1]])

# Creación del objeto del juego
juego = nash.Game(jugador1, jugador2)

# Encontrar los equilibrios de Nash del juego
equilibrios = juego.support_enumeration()

# Imprimir los equilibrios de Nash encontrados
print("Equilibrios de Nash del juego:")
for eq in equilibrios:
    print(eq)
