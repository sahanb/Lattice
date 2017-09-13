︠ed09673d-85ad-48b8-a701-3b90fe4132a1s︠
from math import *
import numpy as np

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

# calculating mu21
def calmu21(b1,b2):
    return round(innerproduct(b1,b2)/norm(b1)**2,2)

#calculate mu32
def calmu32(b1,b2,b3):
#    return innerproduct(b2,b3)/norm(b2)**2
    return round(innerproduct(calb2(b1,b2),b3)/norm(calb2(b1,b2))**2,2)

#calculate mu31
def calmu31(b1,b3):
    return round(innerproduct(b1,b3)/norm(b1)**2,2)
 
# Calculating b2 vector
def calb2(b1,b2):
    l=[]
    mu21 = calmu21(b1,b2)
    for i in range(len(b1)):
        l.append(b2[i]-mu21*b1[i])
    return l

# calculate b3 vector
def calb3(b1,b2,b3):
    l=[]
    mu32=calmu32(b1,b2,b3)
    mu31=calmu31(b1,b3)
    for i in range(len(b1)):
        l.append(b3[i]-mu31*b1[i]-mu32*calb2(b1,b2)[i])
    return l



# compute GSO

def gso(b1,b2,b3):
    return b1,calb2(b1,b2),calb3(b1,b2,b3)


gso([-1,-1,2],[4,0,-1],[0,-2,-3])