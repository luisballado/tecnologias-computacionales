from distribuciones import *

#Constructor clase factory
d = DistribucionFactory()
"""
#Binomial
datos = {}
datos['n'] = 100
datos['p'] = 0.5
binomial = d.getDistribution("Binomial",datos)
binomial.get_graph(100,False)
"""
"""
#Poisson
datos = {}
datos['mu']=2
poisson = d.getDistribution("Poisson",datos)
poisson.get_graph(100,False)
"""
"""
#Exponencial
datos = {}
datos['alpha']=2
exponencial = d.getDistribution("Exponencial",datos)
exponencial.get_graph(100,True)
"""
"""
#Geometrica
datos = {}
datos['p']=0.80
geometrica = d.getDistribution("Geometrica",datos)
geometrica.get_graph(100,True)
"""

#Normal
normal = d.getDistribution("Normal",{})
normal.get_graph(100,3.1400,1.1214,True)
#print(normal.get_probability(3,4.11,1.37))

