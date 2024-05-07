# Pablo Dario Jimenez Nu*o 21310143

class ValorInformacion:
    def __init__(self, modelo, decision, evidencia):
        self.modelo = modelo
        self.decision = decision
        self.evidencia = evidencia

    def calcular_valor_informacion(self, variable):
        # Calculamos el valor de la información para una variable dada
        valor_informacion = 0
        valores_posibles = self.modelo.get_cardinality([variable])[variable]

        for valor in range(valores_posibles):
            evidencia_actualizada = self.evidencia.copy()
            evidencia_actualizada[variable] = valor

            # Calculamos la utilidad esperada dado el valor de la variable
            utilidad_esperada = self.calcular_utilidad_esperada(evidencia_actualizada)

            # Calculamos el valor de la información para este valor de la variable
            valor_informacion += (1 / valores_posibles) * utilidad_esperada

        return valor_informacion

    def calcular_utilidad_esperada(self, evidencia_actualizada):
        # Calculamos la utilidad esperada dada la evidencia actualizada
        inferencia = self.modelo.get_inference_instance()
        resultados = inferencia.query(variables=[self.decision], evidence=evidencia_actualizada)
        utilidad_esperada = resultados.values[self.decision]

        return utilidad_esperada

# Ejemplo de uso
if __name__ == "__main__":
    from pgmpy.models import BayesianModel
    from pgmpy.factors.discrete import TabularCPD

    # Definimos la estructura de la red de decisión
    modelo = BayesianModel([('S', 'D'), ('R', 'D'), ('D', 'L'), ('D', 'G')])

    # Definimos las distribuciones de probabilidad condicional (CPDs)
    cpd_s = TabularCPD(variable='S', variable_card=2, values=[[0.6], [0.4]])
    cpd_r = TabularCPD(variable='R', variable_card=2, values=[[0.8], [0.2]])
    cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
                       evidence=['S', 'R'], evidence_card=[2, 2])
    cpd_l = TabularCPD(variable='L', variable_card=2, values=[[0.99, 0.4], [0.01, 0.6]],
                       evidence=['D'], evidence_card=[2])
    cpd_g = TabularCPD(variable='G', variable_card=2, values=[[0.9, 0.2], [0.1, 0.8]],
                       evidence=['D'], evidence_card=[2])

    # Agregamos las CPDs al modelo
    modelo.add_cpds(cpd_s, cpd_r, cpd_d, cpd_l, cpd_g)

    # Definimos la decisión y la evidencia
    decision = 'G'
    evidencia = {'S': 1, 'R': 1}

    # Creamos una instancia del Valor de la Información
    voi = ValorInformacion(modelo, decision, evidencia)

    # Calculamos el valor de la información para la variable 'D' (Diagnóstico)
    valor_informacion_d = voi.calcular_valor_informacion('D')
    print("Valor de la información para la variable 'D':", valor_informacion_d)
