from abc import ABC, abstractmethod
import math
import numpy as np
import random
from scipy.integrate import quad
import scipy.special as sc
import matplotlib.pyplot as plt
import pandas as pd

#Abstract class
class DISTRIBUCION(ABC):
    
    @abstractmethod
    def get_probability(self):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_probability_cdf(self):
        pass
    
class Binomial(DISTRIBUCION):
        
    def __init__(self,data):
        self.n = data['n']
        self.p = data['p']
        self.x = data['x']
        self.acumulada = data['acumulada']
        
    def get_combinations(self,x=0):
        return (math.factorial(self.n))/(math.factorial(self.n-x)*math.factorial(x))
        
    def get_probability(self,x=0):
        comb = self.get_combinations(x)
        res = comb * self.p**x*(1-self.p)**(self.n-x)
        return res

    def get_probability_cdf(self,k):
        return (sc.betainc(self.n-k,k+1,1-self.p))
    
    #Aplicamos el método del rechazo
    def get_sample(self, cardinality):

        sample = []

        for i in range(cardinality):
            u=random.random()
            k=0
            f=self.get_probability(k)
            while True:
                f+=self.get_probability(k)
                if(f>u):
                    break
                k=k+1
            sample.append(k)
        return sample

class Poisson(DISTRIBUCION):
    
    def __init__(self,data):
        self.mu = data['mu']
        self.acumulada = data['acumulada']
        
    def get_probability(self,x):
        e=math.e
        return (self.mu**x)*(math.exp(-self.mu))/(math.factorial(x))

    #Aplicamos el método del rechazo
    def get_sample(self, cardinality):
        sample=[]
        for i in range(cardinality):
            while True:
                u=random.randint(0,10)
                fu=random.randint(0,10)
                x=random.randint(0,10)
                fz=self.get_probability(x)
                if(fu<=fz):
                    sample.append(u)
                    break
        return sample

    def get_probability_cdf(self,k):
        return (sc.gammainc(self.mu,k))
        
class Geometrica(DISTRIBUCION):
    def __init__(self,data):
        self.p = data['p']
        self.acumulada = data['acumulada']
        
    def get_probability(self,x):
        return ((1-self.p)**x)*self.p

    def get_sample(self,cardinality):
        sample = []
        for i in range(cardinality):
            while True:
                u = random.randint(0,10)
                fu = random.randint(0,10)
                f = self.get_probability(u)
                if (fu<=f):
                    sample.append(u)
                    break
        return sample

    def get_probability_cdf(self,x):
        return (1-(1-self.p)**(x+1))
        
class Exponencial(DISTRIBUCION):
    def __init__(self,data):
        self.alpha = data['alpha']
        self.acumulada = data['acumulada']
        
    def get_probability(self,x):
        return self.alpha*math.exp(-self.alpha*x)
    
    def get_sample(self,cardinality):
        sample = []
        for i in range(cardinality):
            while True:
                u = random.uniform(0,5)
                fu = random.uniform(0,5)
                f = self.get_probability(u)
                if (fu<=f):
                    sample.append(u)
                    break
        return sample

    def get_probability_cdf(self,x):
        return 1-math.exp(-self.alpha*x)
    
class Normal(DISTRIBUCION):
    def __init__(self,data):
        self.mu = data['mu']
        self.sigma = data['sigma']
        self.acumulada = data['acumulada']
    
    #Ojo esta es función es la normal estandarizada    
    def get_distribution(self, z):
        coef=1/(math.sqrt(2*(math.pi)))
        exp=math.exp(-0.5*pow((z),2))
        return (coef*exp)  

    """
    def get_probability(self,x):
        z=(x-self.mu)/self.sigma
        p=quad(self.get_distribution,np.NINF, z)
        return p[0]
    """
    
    def get_probability(self,x):
        return (1/(self.sigma*math.sqrt(math.pi*2)))*math.exp(-0.5*(((x-self.mu)/self.sigma)**2)) 
    
    #Aplicamos el método del rechazo
    def get_sample(self, cardinality):
        sample=[]
        for i in range(cardinality):
            while True:
                u=random.uniform(-5,5)
                fu=random.uniform(-5,5)
                fz=self.get_probability(u)
                if(fu<=fz):
                    sample.append(u)
                    break
        return sample
    
    def get_probability_cdf(self,x):
        return  0.5*(1+math.erf((x-self.mu)/(self.sigma*math.sqrt(2))))
    
class DistribucionFactory:

    def __init__(self):
        pass

    def getDistribution(self, type, parameters:dict):
        if type=="Binomial":
            return Binomial(parameters)
        elif type=="Poisson":
            return Poisson(parameters)
        elif type=="Geometrica":
            return Geometrica(parameters)
        elif type=="Exponencial":
            return Exponencial(parameters)
        elif type=="Gausiana":
            return Gausiana(parameters)
        else:
            return Normal(parameters)
