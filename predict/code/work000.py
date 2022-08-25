# -*- coding: utf-8 -*-
import numpy as np
import os
from os import path

def f(x,p):
    def _Z(x,a,b):
        Z1 = (x[3]*np.exp(-2*x[1]))/np.power(b+a*np.exp(-x[1]),2)
        Z2 = (x[2]*np.exp(-2*x[0]))/np.power(a+b*np.exp(-x[0]),2)
        return Z1+Z2
    def _ff(X,a,b,c):
        return (np.exp((a**2/c)*X)-b)**2
    X1 = _Z(x,p[0],p[1])
    X2 = _Z(np.array([x[1],x[0],x[3],x[2]]),p[0],p[1])
    f = _ff(X1,p[0],p[2],p[4]) + _ff(X2,p[1],p[3],p[4])
    return f, X1, X2

def convex_function(u, v, p, lambda_):
    uv = (1-lambda_)*u+lambda_*v
    (f_uv,tmp,tmp) = f(uv,p)
    (f_u,tmp,tmp) = f(u,p)
    (f_v,tmp,tmp) = f(v,p)
    F = f_uv -(1-lambda_)*f_u-lambda_*f_v
    return F

    
def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

        
def main():
    # sample: f
    v = 2*np.ones(4)
    p = np.array([1, 1, 1, 1, 1])
    (pp,tmp,tmp) = f(v,p)
    print(pp)

    # meshgrid
    x = np.arange(0, 4)
    y = np.arange(0, 4)
    z = np.arange(0, 4)
    w = np.arange(0, 4)

    (xx, yy, zz, ww) = np.meshgrid(x,y,z,w)
    allsize = xx.size
    xx=xx.reshape(allsize,1)
    yy=yy.reshape(allsize,1)
    zz=zz.reshape(allsize,1)
    ww=ww.reshape(allsize,1)
    X = np.hstack((xx,yy,zz,ww))
    x_list = [list(u) for u in X]

    # convex: each sample
    lambda_list = np.arange(0.1, 1, 0.1)
    for xx in x_list:
        print(xx)
        F = [convex_function(np.array(xx), v, p, lambda_) for lambda_ in lambda_list]
        print('convex: ', np.where(np.array(F)<0, True, False))

    # sample: u, v, uv
    u = np.array([2,2,1,3])
    uv = np.array([2,2,2,2.5])
    (f_u,X1_u,X2_u) = f(u,p)
    (f_v,X1_v,X2_v) = f(v,p)
    (f_uv,X1_uv,X2_uv) = f(uv,p)
    print(f_u,X1_u,X2_u)
    print(f_v,X1_v,X2_v)
    print(f_uv,X1_uv,X2_uv)

    
if __name__ == "__main__":
    main()
