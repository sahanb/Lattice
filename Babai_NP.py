from math import *
import copy
import numpy as np


def mul(x,y):
    return [x[i]*y[i] for i in range(len(x))]

def add(x,y):
    return [x[i]+y[i] for i in range(len(x))]

def sub(x,y):
    return [x[i]-y[i] for i in range(len(x))]

def k_mul(k,x):
    return [k*xx for xx in x]

def dot(x,y):
    return sum(mul(x,y))

def f(x,y):
    return dot(x,y)/dot(y,y)

def norm(b):
    x=0
    for i in range(len(b)):
        x=x+b[i]**2

    return sqrt(x)

def lll(b,delta):
    flg=True
    n=len(b)
    while flg:

        b_=[]
        mu=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            tb=copy.copy(b[i])
            for j in range(i):
                mu[i][j]=f(b[i],b_[j])
                tb=sub(tb,k_mul(mu[i][j],b_[j]))
            b_.append(tb)
  #      print(mu)
    #    print(b_)
        for i in range(n):
            for j in reversed(range(i)):
                c=round(mu[i][j])
                b[i]=sub(b[i],k_mul(c,b[j]))
  #      print(mu)

        flg=False
        for i in range(n-1):
            if dot(b[i+1],b[i+1])<(delta-f(b[i+1],b[i])**2)*dot(b[i],b[i]):
                b[i],b[i+1]=b[i+1],b[i]
                flg=True
                break
    #print(b)
    return b,b_




def babainp(w,b,delta):
    ww = copy.copy(w)
    bb,bs = lll(b,delta)
#    print(bb,bs)

    tt=[]
    vv = [0 for i in range(len(bb))]
    for i in reversed(range(len(bs))):
        ti = f(ww,copy.deepcopy(bs[i]))
        tt.append(ti)
        vi= k_mul(round(ti),bb[i])
        vv = add(vv,vi)
 #       vv.append(vi)
        ww = sub(sub(ww,(k_mul(ti-round(ti),bs[i]))),vi)

 #       print(vv)
#    print("distance to t")
    print(w,vv)

    return norm(sub(w,vv))


def input2d():
    print("Enter columns of the Input Matrix:")
    a=input()
    b=list(a[2:-2].split('],['))
    c=list(map(lambda s:list(map(float,s.split(','))),b))
    return c

def input1d():
    print("Enter the w or t vector:")
    a=input()
    b=list(map(float,a[1:-1].split(',')))
    return b


#b = input2d()
b = eval(input("Enter the input Matrix:"))
#w = input1d()
w = eval(input("Enter the w or t vector:"))
#delta = (input("Enter the Delta value in decimal format: "))
delta = eval(input("Enter the Delta value:"))
print("Distance to vector t: ")
print(babainp(w,b,delta))
#babainp([5,7,-9],[[-1,-1,2],[4,0,-1],[0,-2,-3]],3/4)
#print(babainp([5,7,-9],[[-1,-1,2],[4,0,-1],[0,-2,-3]],3/4))
