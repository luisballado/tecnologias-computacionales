from abc import ABC, abstractmethod
import math
import numpy as np
import random
from scipy.integrate import quad
import matplotlib.pyplot as plt
import pandas as pd

__author__ = "Luis Ballado"

#Abstract class
class DISTRIBUCION(ABC):
    
    @abstractmethod
    def get_probability(self):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_graph(self):
        pass
    
class Binomial(DISTRIBUCION):
        
    def __init__(self,data):
        self.n = data['n']
        self.p = data['p']

    def get_combinations(self,x=0):
        return (math.factorial(self.n))/(math.factorial(self.n-x)*math.factorial(x))
        
    def get_probability(self,x=0):
        comb = self.get_combinations(x)
        res = comb * self.p**x*(1-self.p)**(self.n-x)
        return res

    #Aplicamos el método del rechazo
    def get_sample(self, cardinality):
        sample=[]
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
        
    def get_graph(self,cardinality,scatter):
        sample = pd.DataFrame(self.get_sample(cardinality),columns=['n_gen'])
        sample['pdf'] = sample['n_gen'].apply(lambda x: self.get_probability(x))
        if scatter:
            plt.scatter(sample['n_gen'],sample['pdf'])
        else:
            plt.stem(sample['n_gen'],sample['pdf'])
        plt.savefig('binomial.png')
        
class Poisson(DISTRIBUCION):
    
    def __init__(self,data):
        self.mu = data['mu']
        
    def get_probability(self,x):
        e=math.e
        return (self.mu**x)*(e**(-1*self.mu))/(math.factorial(x))

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
    
    def get_graph(self,cardinality,scatter):
        sample = pd.DataFrame(self.get_sample(cardinality),columns=['n_gen'])
        sample['pdf'] = sample['n_gen'].apply(lambda x: self.get_probability(x))
        if scatter:
            plt.scatter(sample['n_gen'],sample['pdf'])
        else:
            plt.stem(sample['n_gen'],sample['pdf'])
        plt.savefig('poisson.png')
        
class Geometrica(DISTRIBUCION):
    def __init__(self,data):
        self.p = data['p']

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

    def get_graph(self,cardinality,scatter):
        sample = pd.DataFrame(self.get_sample(cardinality),columns=['n_gen'])
        sample['pdf'] = sample['n_gen'].apply(lambda x: self.get_probability(x))
        if scatter:
            plt.scatter(sample['n_gen'],sample['pdf'])
        else:
            plt.stem(sample['n_gen'],sample['pdf'])
        plt.savefig('geometrica.png')
            
class Exponencial(DISTRIBUCION):
    def __init__(self,data):
        self.alpha = data['alpha']

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

    def get_graph(self,cardinality,scatter):
        sample = pd.DataFrame(self.get_sample(cardinality),columns=['n_gen'])
        sample['pdf'] = sample['n_gen'].apply(lambda x: self.get_probability(x))
        if scatter:
            plt.scatter(sample['n_gen'],sample['pdf'])
        else:
            plt.stem(sample['n_gen'],sample['pdf'])
        plt.savefig('exponencial.png')
                
class Normal(DISTRIBUCION):
    def __init__(self,data):
        pass
    
    #Ojo esta es función es la normal estandarizada    
    def get_distribution(self, z):
        coef=1/(math.sqrt(2*(math.pi)))
        exp=np.exp(-0.5*pow((z),2))
        return (coef*exp)  
    
    def get_probability(self,x,mu,sigma):
        z=(x-mu)/sigma
        p=quad(self.get_distribution,np.NINF, z)
        return p[0]
    
    #Aplicamos el método del rechazo
    def get_sample(self, cardinality, mu,sigma):
        sample=[]
        for i in range(cardinality):
            while True:
                u=random.random()
                fu=random.random()
                z=(u-mu)/sigma
                fz=self.get_distribution(z)
                if(fu<=fz):
                    sample.append(u)
                    break
        return sample

    def get_graph(self,cardinality,mu,sigma,scatter):
        sample = pd.DataFrame(self.get_sample(cardinality,mu,sigma),columns=['n_gen'])
        sample['pdf'] = sample['n_gen'].apply(lambda x: self.get_probability(x,mu,sigma))
        if scatter:
            plt.scatter(sample['n_gen'],sample['pdf'])
        else:
            plt.stem(sample['n_gen'],sample['pdf'])
        plt.savefig('gausiana.png')
        
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
