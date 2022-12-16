from distribuciones import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Constructor clase factory
d = DistribucionFactory()


#datos
datos = {}
datos['mu']=4.11
datos['sigma']=1.37


#El get_sample regresará valores que cumplen la distribucion

#para graficar se debe evaluar cada valor con su funcion get_probability pasandole el X

#Normal/Gausiana
#Operaciones correctas
"""
normal = d.getDistribution("Normal",{})
#normal.get_graph(normal.get_sample(5))
datos = normal.get_sample(10,datos['mu'],datos['sigma'])
#print(normal.get_probability(3,4.11,1.37))
algo = lambda x: (normal.get_probability(i) for i in datos)

print(list(algo))
"""

#Binomial
#Operaciones correctas
"""
d_binom = {}
d_binom['n'] = 9
d_binom['p'] = 0.8
binomial = d.getDistribution("Binomial",d_binom)
#print(binomial.get_sample(30))
#binomial.get_graph(binomial.get_sample(30))
print(binomial.get_probability(6))
"""

#Geometrica
#Operaciones correctas
"""
d_geom = {}
d_geom['p'] = 0.4
geometrica = d.getDistribution("Geometrica",d_geom)
#numeros = geometrica.get_sample(100)
#print(numeros)
#geometrica.get_graph(numeros,list(range(0,100)))
print(geometrica.get_probability(3))
"""

#Poisson
#Operaciones correctas

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
d_poisson = {}
d_poisson['mu'] = 6
poisson = d.getDistribution("Poisson",d_poisson)
#poisson.get_graph(poisson.get_sample(28,))
print(poisson.get_probability(6))
"""

#Exponencial
#Operaciones correctas

d_exp = {}
d_exp['lam'] = 0.25
exponencial = d.getDistribution("Exponencial",d_exp)

sample = pd.DataFrame(exponencial.get_sample(10),columns=["n_gen"])

sample["PDF"]=sample["n_gen"].apply(lambda x: exponencial.get_probability(x))


plt.scatter(sample["n_gen"],sample["PDF"])
#print(exponencial.get_probability(5))

#Normal
normal = d.getDistribution("Normal",{})
normal.get_graph(100,3.1400,1.1214,True)
#print(normal.get_probability(3,4.11,1.37))


