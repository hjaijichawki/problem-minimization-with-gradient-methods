import numpy as np

def A(n:int):
    '''This function is used to define the matrix A
       :param n: the number of rows and columns in this matrix'''
    A=2*np.eye(n)-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
    return(A*(n+1)**2)


def J(u,fx):
    n=np.size(u)
    A=(n+1)**2*(2*np.eye(n)-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1))
    J=(0.5)*np.dot((A@u),u)-np.dot(fx,u)
    return J


def DJ(U,fx):
    n=np.size(U)
    A1=A(n)
    return (np.dot(A1,U)-fx)


def f(x):
    return np.ones(np.size(x))

def g(x):
    v=1.5-20*(x-0.6)**2
    v[v<0]=0
    return v

def J(A,u,b):
    return (1/2)*np.dot(np.transpose(u),(np.dot(A,u)))-np.dot(np.transpose(b),u)