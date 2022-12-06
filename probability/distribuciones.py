from abc import ABC, abstractmethod
import math
import numpy as np
import random
from scipy.integrate import quad
import matplotlib.pyplot as plt

__author__ = "Luis Ballado"

#Abstract class
class DISTRIBUCION(ABC):
    
    @abstractmethod
    def get_distribution(self):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_graph(self):
        pass
    
class Binomial(DISTRIBUCION):
    """
    Binomial distribution is a probability distribution 
    that summarises the likelihood that a variable will take 
    one of two independent values under a given set of parameters.

    Attributes
    ----------
    n : int
        numero de ensayos
    p : float
        probabilidad de un exito en cualquiera de los ensayos
    
    Methods
    -------
    get_distribution(sound=None)
        Prints the animals name and what sound it makes
    """
    
    def __init__(self,dictionary):
        """
        Parametros
        ----------
        n : int
            The n variable
        p : int
            The p variable
        """
        self.n = dictionary['n']
        self.p = dictionary['p']

    def get_combinations(self,r=0):
        """Gets and prints the spreadsheet's header columns
        
        Args:
            file_loc (str): The file location of the spreadsheet
        print_cols (bool): A flag used to print the columns to the console
        (default is False)
        
        Returns:
            list: a list of strings representing the header columns
        """

        return (math.factorial(self.n))/(math.factorial(self.n-r)*math.factorial(r))
        
    def get_distribution(self,r=0):
        """
        Args:
            x exitos
        """
        comb = self.get_combinations(r)
        res = comb * self.p**r*(1-self.p)**(self.n-r)
        print(res)
        return res

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
    
    def get_graph(self):
        print("Dibujar grafica Binomial")
        

class Poisson(DISTRIBUCION):
    ''' Poisson distribution is the discrete probability distribution 
    which represents the probability of occurrence of an event r number 
    of times in a given interval of time or space if these events occur 
    with a known constant mean rate and are independent of each other. 
    This type of probability is used in many cases where events occur 
    randomly, but with a known average rate. The number of events that 
    happen during an interval is dependent on the time elapsed rather 
    than the total time available.'''
    def __init__(self,data):
        self.k = data['k']
        self.mu = data['mu']
        
    def get_distribution(self):
        e=2.71828
        print("get_distribution")
        return (self.mu**self.k)*(e**(-1*self.mu))/(math.factorial(self.k))

    #Aplicamos el método del rechazo
    def get_sample(self, cardinality, k, mu):
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
    
    def get_graph(self):
        print("Dibujar grafica Poisson")
        
class Geometrica(DISTRIBUCION):
    def __init__(self,data):
        pass

    def get_distribution(self):
        return 0

    def get_sample(self):
        print("Hola Geometrica")
        return 0

    def get_graph(self):
        print("Dibujar grafica Geometrica")
    
class Exponencial(DISTRIBUCION):
    def __init__(self,data):
        pass

    def get_distribution(self):
        print("get_distribution")
        return 0
        
    def get_sample(self):
        print("Hola Exponencial")
        return 0

    def get_graph(self):
        print("Dibujar grafica Exponencial")
        
class Gausiana(DISTRIBUCION):
    def __init__(self,data):
        pass

    def get_distribution(self):
        print("get_distribution")
        return 0
        
    def get_sample(self):
        print("Hola Gausiana")
        return 0

    def get_graph(self):
        print("Dibujar grafica Gausiana")

class Normal(DISTRIBUCION):
    def __init__(self,data):
        pass
    
    #Ojo esta es función es la normal estandarizada    
    def get_distribution(self, z):
        coef=1/(math.sqrt(2*(math.pi)))
        exp=np.exp(-0.5*pow((z),2))
        return (coef*exp)  
    
    def getProbability(self,x,mu,sigma):
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

    def get_graph(self,data):
        print("Dibujar grafica Normal")
        xpoints = np.array([0,1,2,3,4])
        ypoints = np.array(data)
        plt.plot(xpoints,ypoints)
        plt.savefig('foo.png')
        pass
    
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
"""
d = Binomial(n=6,p=0.6)

print(d.n)
print(d.getdistribution(2))

d_poisson = DPoisson(k=5,mu=7)
print(d_poisson.get_distribution())
"""
