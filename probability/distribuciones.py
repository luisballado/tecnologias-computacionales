import math

class DBinomial(object):
    ''' Binomial distribution is a probability distribution 
    that summarises the likelihood that a variable will take 
    one of two independent values under a given set of parameters.'''
    
    def __init__(self,n,p):
        self.n=n
        self.p=p
        
    def get_combinations(self,r=0):
        return (math.factorial(self.n))/(math.factorial(self.n-r)*math.factorial(r))
        
    def getdistribution(self,r):
        comb = self.get_combinations(r)
        return comb * self.p**r*(1-self.p)**(self.n-r)

class DPoisson(object):
    ''' Poisson distribution is the discrete probability distribution 
    which represents the probability of occurrence of an event r number 
    of times in a given interval of time or space if these events occur 
    with a known constant mean rate and are independent of each other. 
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
    
d = DBinomial(n=6,p=0.6)

print(d.n)
print(d.getdistribution(2))

d_poisson = DPoisson(k=5,mu=7)
print(d_poisson.get_distribution())
