# En este archivo estaran implementadas todas las operaciones elementales usadar en
# cada algorithmo
import numpy as np
def turn(x,y,z): #x,y,z son puntos del plano ordenados
    M = np.array([[y[0]-x[0],z[0]-y[0]],[y[1]-x[1],z[1]-y[1]]])
    det = np.linalg.det(M)
    if det > 0:
        return 'R'
    elif det < 0:
        return 'L'
    return 'A'
print(turn((0,0),(1,0),(0,1)))
