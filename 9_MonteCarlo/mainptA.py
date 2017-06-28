from __future__ import division
import numpy as np
from montecarlo import *


print "###### Task A ######"
print "Monte Carlo integration:"
pii = np.pi
def f1(x):
	f = 1/((1 - np.cos(x[0]) * np.cos(x[1]) * np.cos(x[2])) * np.power(pii,3))
	return f
a1 = np.array([0,0,0])
b1 = np.array([pii,pii,pii])
N  = np.power(10,7)

vec1,error1 = monte(f1,a1,b1,N)


print "Calculate the integral given in the assignment"
print "Monte carlo with N=10^7:", vec1
print "The result given is", 1.3932039296856768591842462603255
