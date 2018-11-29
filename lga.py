
from math import *

# Calculating norm
def norm(b):
    x=0
    for i in range(len(b)):
        x=x+b[i]**2

    return sqrt(x)



# inner product function
def innerproduct(c,d):
    x=0
    for i in range(len(c)):
        x=x+c[i]*d[i]
    return x


# calculating mu
def calmu(b1,b2):
    return round(innerproduct(b1,b2)/innerproduct(b1,b1),0)
    
# Calculating b2 vector
def calb2(b1,b2):
    l=[]
    mu = calmu(b1,b2)
    for i in range(len(b1)):
        l.append(b2[i]-mu*b1[i])
    return l


# Lagrange Gauss Algorithm
def LGA(b1,b2):

    b2=calb2(b1,b2)
    
    while norm(b2)<norm(b1):
        b1,b2=b2,b1
        b2=calb2(b1,b2)
    print (b1,b2)
        
    
