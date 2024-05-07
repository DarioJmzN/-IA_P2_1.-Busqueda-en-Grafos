# Pablo Dario Jimenez Nu*o 21310143

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Definición de la Red Bayesiana Dinámica (DBN)
dbn = DBN()

# Definición de las variables y sus relaciones temporales
dbn.add_edges_from([(('X0', 0), ('X1', 0)), (('X0', 0), ('X2', 0)), (('X1', 0), ('X2', 0))])

# Definición de las probabilidades condicionales (CPDs)
cpd_X0 = TabularCPD(('X0', 0), 2, values=[[0.5], [0.5]])
cpd_X1 = TabularCPD(('X1', 0), 2, values=[[0.6], [0.4]], evidence=[('X0', 0)], evidence_card=[2])
cpd_X2 = TabularCPD(('X2', 0), 2, values=[[0.7, 0.3], [0.2, 0.8]], evidence=[('X0', 0), ('X1', 0)], evidence_card=[2, 2])

# Añadir las CPDs a la DBN
dbn.add_cpds(cpd_X0, cpd_X1, cpd_X2)

# Inferencia en la DBN
inference = DBNInference(dbn)

# Calcular la probabilidad de un estado en el tiempo 1 dado el estado en el tiempo 0
print("Probabilidad de (X1=1) dado (X0=0):", inference.query(variables=[('X1', 0)], evidence={'X0': 0})[('X1', 0)].values[1])
