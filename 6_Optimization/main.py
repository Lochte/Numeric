import numpy as np
import counter
from equations import *
from minimization import *
import sys
sys.path.append('/Users/AndersLochte/Documents/numerical/5_rootfinding')
from findroots import *
from rootcounter import *
sys.path.append('/Users/AndersLochte/Documents/numerical/4_LSQfit')
from LSbyQR import *


x0 = np.array([-5.,6.])
print "###### Task A ######"
print "Starting points=",x0
counter.calls=0
rosenmini=newtonmini(rosen, x0, gradrosen, Hessrosen)
print "Minima of Rosenbrock's valley function:"
print rosenmini
print "steps:"
print counter.calls
print "\n"

x1=np.array([-4.,8.])
counter.calls=0
print "Starting points=",x1
himmelmini=newtonmini(himmel, x1, gradhimmel, Hesshimmel)
print "Minima of Himmelblau function:"
print himmelmini
print "steps:"
print counter.calls
print "\n"

print "###### Task B ######"
x0 = np.array([0.5,2.])
print "Starting points=",x0
counter.calls=0
rosenmini=quasinewton(rosen, x0, gradrosen)
print "Minima of Rosenbrock's valley function:"
print rosenmini
print "steps:"
print counter.calls
print "\n"


x1=np.array([-2.,3.])
counter.calls=0
print "Starting points=",x1
himmelmini=quasinewton(himmel, x1, gradhimmel)
print "Minima of Himmelblau function:"
print himmelmini
print "steps:"
print counter.calls
print "\n"


eps = 1e-12
x_0 = np.array([-4.,8.])
dx = np.array([1e-8,1e-8])

rootcounter.calls = 0

res = newtons(gradrosen, x_0, dx, eps)
print "Rootfinding newtons method. Roots of Rosenbrock's gradient function:"
print res
print rootcounter.calls

rootcounter.calls = 0
res = newtons(gradhimmel, x_0, dx, eps)
print "Rootfinding newtons method. Roots of Himmelblau gradient function:"
print res
print rootcounter.calls
print "Rootfinding is not as efficient."

t = [0.23,1.29,2.35,3.41,4.47,5.53,6.59,7.65,8.71,9.77]
y = [4.64,3.38,3.01,2.55,2.29,1.67,1.59,1.69,1.38,1.46]
e = [0.42,0.37,0.34,0.31,0.29,0.27,0.26,0.25,0.24,0.24]
