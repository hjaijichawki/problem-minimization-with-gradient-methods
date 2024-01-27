import numpy as np

def check(n):
    A=2*np.eye(n)-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
    L=np.linalg.eigvals(A)
    for i in L:
        if i>0 :
           continue;
        else:
                print("The matrix is not positive definite")
                return
    print("The matrix A is positive definite")
    return A