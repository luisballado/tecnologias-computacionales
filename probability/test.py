from distribuciones import *

#Constructor clase factory
d = DistribucionFactory()

#datos
datos = {}
datos['p']=0.80

#Binomial
"""
binomial = d.getDistribution("Binomial",datos)
print(binomial.get_probability(x=6))
"""

#Poisson
"""
poisson = d.getDistribution("Poisson",datos)
print(poisson.get_probability(x=5))
"""

#Exponencial
"""
exponencial = d.getDistribution("Exponencial",datos)
print(exponencial.get_probability(0))
"""

#Geometrica
geometrica = d.getDistribution("Geometrica",datos)
sample = pd.DataFrame(geometrica.get_sample(1000),columns=['n_gen'])
sample['PDF']=sample['n_gen'].apply(lambda x: geometrica.get_probability(x))

plt.scatter(sample['n_gen'],sample['PDF'])
plt.savefig('geometrica.png')

"""
#Normal
normal = d.getDistribution("Normal",{})
print(normal.get_probability(3,4.11,1.37))
"""
