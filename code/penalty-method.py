import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import minimize
import numpy.linalg as li

def Penalty(n,eta):   
    u=np.zeros(n)
    a=A(n)
    b=np.ones(n)
    k=0
    D,V=li.eig(a)
    p=2/(np.max(D)+np.min(D))
    err=1e-6
    w=np.zeros(n)
    x1=np.array([0,1])
    gn=g(x1)
    start_time=time.time()
    while (err>=1e-6)&(k<=20000):
        for i in range(0,n):
            w[i]=2*max((gn[i]-u[i]),0)    
        d=b-np.dot(a,u)+1/eta*w
        u=u+p*d
        err=p*np.linalg.norm(d)
        k=k+1
    print("eta=",eta)
  
    print("The number of necessary iterations is:")
    print(k)
    end_time = time.time()
    print("The execution time for this script is:")
    print(end_time-start_time)
    print("\n")
    