# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

def policy_iteration(transiciones, recompensas, gamma, politica=None, tol=1e-6):
    num_estados = len(transiciones)
    num_acciones = len(transiciones[0])
    
    # Inicializamos la política aleatoriamente si no se proporciona
    if politica is None:
        politica = np.random.randint(num_acciones, size=num_estados)
    
    while True:
        # Paso de Evaluación de Política
        valores = policy_evaluation(transiciones, recompensas, gamma, politica, tol)
        
        # Paso de Mejora de Política
        politica_estable = True
        for estado in range(num_estados):
            accion_vieja = politica[estado]
            
            # Calculamos la mejor acción según los valores óptimos
            valores_acciones = [sum(transiciones[estado][accion][prox_estado] * (recompensas[estado][accion][prox_estado] + gamma * valores[prox_estado]) 
                                    for prox_estado in range(num_estados)) for accion in range(num_acciones)]
            mejor_accion = np.argmax(valores_acciones)
            
            # Actualizamos la política
            politica[estado] = mejor_accion
            
            # Verificamos si la política ha cambiado
            if accion_vieja != mejor_accion:
                politica_estable = False
        
        # Si la política no cambia, hemos encontrado la política óptima
        if politica_estable:
            break
    
    return politica

def policy_evaluation(transiciones, recompensas, gamma, politica, tol=1e-6):
    num_estados = len(transiciones)
    valores = np.zeros(num_estados)
    
    while True:
        delta = 0
        for estado in range(num_estados):
            v_antiguo = valores[estado]
            accion = politica[estado]
            
            # Calculamos el nuevo valor para el estado según la política actual
            nuevo_valor = sum(transiciones[estado][accion][prox_estado] * (recompensas[estado][accion][prox_estado] + gamma * valores[prox_estado]) 
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

    # Ejecutamos la iteración de políticas
    politica_optima = policy_iteration(transiciones, recompensas, gamma)

    # Imprimimos la política óptima
    print("Política óptima:")
    print(politica_optima)

