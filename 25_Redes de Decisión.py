# Pablo Dario Jimenez Nu*o 21310143

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

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

# Verificamos la validez del modelo
print("¿El modelo es válido?", modelo.check_model())

# Realizamos una inferencia en el modelo utilizando Variable Elimination
inferencia = VariableElimination(modelo)

# Calculamos la probabilidad de que el paciente tenga gripe (G) dado que tiene fiebre (S) y tos (R)
resultado = inferencia.query(variables=['G'], evidence={'S': 1, 'R': 1})
print(resultado)
