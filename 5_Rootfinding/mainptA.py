import numpy as np
from findroots import *
from equations import *

#start conditions
eps = 1e-12
x_0 = np.array([1.,-1.])
dx = np.array([1e-8,1e-8])

res = newtons(eq1, x_0, dx, eps)
print "###### Task A ######"
print "Roots of exp(-x)+exp(-y) = 1+1/A, A=10000:"
print res
print "\n"
rosenres = newtons(rosen,x_0, dx, eps)
print "Roots of Rosenbrock's valley function:"
print rosenres
print "\n"
himmelres = newtons(himmel,x_0, dx, eps)
print "Roots of Himmelblau function:"
print himmelres
print "\n"
