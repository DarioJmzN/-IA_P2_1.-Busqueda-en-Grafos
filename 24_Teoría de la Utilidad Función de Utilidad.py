# Pablo Dario Jimenez Nu*o 21310143

class FuncionUtilidad:
    def __init__(self, parametros):
        self.parametros = parametros

    def calcular_utilidad(self, resultados):
        utilidad = 0
        for i, valor in enumerate(resultados):
            utilidad += self.parametros[i] * valor
        return utilidad

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos una función de utilidad con parámetros arbitrarios
    parametros = [0.5, 0.3, 0.2]
    funcion_utilidad = FuncionUtilidad(parametros)

    # Definimos algunos resultados
    resultados = [10, 5, 8]

    # Calculamos la utilidad utilizando la función de utilidad
    utilidad = funcion_utilidad.calcular_utilidad(resultados)

    # Imprimimos el resultado
    print("La utilidad de los resultados es:", utilidad)
