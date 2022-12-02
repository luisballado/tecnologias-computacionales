from abc import ABC, abstractmethod
import math

__author__ = "Luis Ballado"

#Abstract class
class DISTRIBUCION(ABC):
    
    @abstractmethod
    def get_distribution(self):
        pass

    @abstractmethod
    def get_something(self):
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
    
    def __init__(self,n,p):
        """
        Parameters
        ----------
        
        n : str
            The name of the animal
        p : str
            The sound the animal makes
        """
        self.n = n
        self.p = p

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
        return comb * self.p**r*(1-self.p)**(self.n-r)

    def get_something(self):
        print("Hola")

class Poisson(DISTRIBUCION):
    ''' Poisson distribution represents the probability of occurrence
    of an event r number of times in a given interval of time or space
    if these events occur with a known constant mean rate and are
    independent of each other. 
    This type of probability is used in many cases where events occur 
    randomly, but with a known average rate. The number of events that 
    happen during an interval is dependent on the time elapsed rather 
    than the total time available.'''
    def __init__(self,k=0,mu=0):
        self.k = k
        self.mu = mu
        
    def get_distribution(self):
        e=2.71828
        return (self.mu**self.k)*(e**(-1*self.mu))/(math.factorial(self.k))

    def get_something(self):
        print("Hola")

class Geometrica(DISTRIBUCION):
    def __init__(self):
        pass

    def get_distribution(self):
        return None

    def get_something(self):
        return None

class Exponencial(DISTRIBUCION):
    def __init__(self):
        pass

    def get_distribution(self):
        return None

    def get_something(self):
        return None

class Gausiana(DISTRIBUCION):
    def __init__(self):
        pass

    def get_distribution(self):
        return None

    def get_something(self):
        return None

class DistribucionFactory:
    def __init__(self):
        pass

    def getDistribution(self, type, parameters:dict):
        if type=="Binomial":
            return Binomial(parameters)
        elif type=="Poisson":
            print("Hola")
        elif type=="Geometrica":
            print("Hola")
        elif type=="Exponencial":
            print("Hola")
        elif type=="Gausiana":
            print("Hola")
"""
d = Binomial(n=6,p=0.6)

print(d.n)
print(d.getdistribution(2))

d_poisson = DPoisson(k=5,mu=7)
print(d_poisson.get_distribution())
"""
