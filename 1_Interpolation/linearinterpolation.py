import numpy as np
import search
# linear spline

def linterp(x, y, z):
    ls=np.zeros(len(z))
    dx = x[1:] - x[0:-1]
    dy = y[1:] - y[0:-1]

    for i in range(len(z)):
        l = search.bin(x,z[i])
        ls[i] = y[l]+(z[i]-x[l])*(dy[l]/dx[l])

    return ls
