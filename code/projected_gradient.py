import numpy as np
import math

def projk(u,g):
    import numpy as np
    k=np.maximum(u,g)
    return(k)


def projected_gradient_fixed_step (J, DJ , gn , u0 , rho , Tol , iterMax , store ):
    k=0
    r=Tol
    u=[u0]
    while((r>=Tol)&(k<iterMax)):
        w=-DJ(u0)
        uo=u0
        u0=projk(u0+rho*w,gn(u0))
        u.append(u0)
        r=np.sqrt(np.dot(u0-uo),np.dot(u0-uo))
        k+=1
    if (store==0):
        return(u0,k)
    elif (store==1):
        return(u,k)
    

def fixed_step(J, DJ , gn , u0 , rho , Tol , iterMax , store):
     k=0
     l1=[u0[0]]
     l2=[u0[1]]
     r=Tol
     u0=u0
     while(r>=Tol) and (k<=iterMax):
       w=-DJ(u0)
       uo=u0
       u0=projk(u0+rho*w,gn(u0))
       l1.append(u0[0])
       l2.append(u0[1])
       r=math.sqrt(np.dot(u0-uo,u0-uo))
       k+=1
     if (store==0):
        return(l1[-1],l2[-1],k)
     elif (store==1):
        return(l1,l2,k)