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
