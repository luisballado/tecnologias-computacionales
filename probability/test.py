from distribuciones import *

#Constructor clase factory
d = DistribucionFactory()

#datos
datos = {}
datos['n']=3
datos['p']=.50

"""
#Binomial
binomial = d.getDistribution("Binomial",datos)
binomial.get_distribution()
binomial.get_sample()
binomial.get_graph()

datos = {}
datos['k']=3
datos['mu']=.50

#Exponencial
exponencial = d.getDistribution("Exponencial",datos)
exponencial.get_distribution()
exponencial.get_sample()
exponencial.get_graph()

#Geometrica
geometrica = d.getDistribution("Geometrica",datos)
geometrica.get_distribution()
geometrica.get_sample()
geometrica.get_graph()

#Gausiana
gausiana = d.getDistribution("Gausiana",datos)
gausiana.get_distribution()
gausiana.get_sample()
gausiana.get_graph()

#Poisson
poisson = d.getDistribution("Poisson",datos)
poisson.get_distribution()
poisson.get_sample()
poisson.get_graph()
"""

#Normal
normal = d.getDistribution("Normal",datos)
normal.get_graph(normal.get_sample(5,38.8,11.4))

