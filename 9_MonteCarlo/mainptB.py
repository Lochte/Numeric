from __future__ import division
import numpy as np
from montecarlo import *
import matplotlib.pyplot as plt


print "###### Task B ######"
pii = np.pi
def f2(x):
	f = np.cos(x[0])*np.power(x[1],2)
	return f
a2 = np.array([0,0,0])
b2 = np.array([pii/2,3,1])
N1 = [10,100,1000,10000,100000,1000000]
n  = 6
t  = list(range(10,1000000))
error2 = np.zeros(n)
vec2=np.zeros(n)
for i in range(n):
	N=np.power(10,i+1)
	vec2[i],error2[i]=monte(f2,a2,b2,N)
print "Calculate the integral cos(x)*y^2 from 0 to pi/2 and 0 to 3"
print "Monte Carlo with N from 10^1 to 10^7:"
print vec2
print "Exact result:", 9
plt.figure()
plt.title("Plot of error as function of N")
plt.loglog(N1,error2,'x',label="error as function of N")
plt.loglog(t,9./np.sqrt(t),label="fit: a/sqrt(N)")
plt.legend(loc=1)
plt.savefig('MonteCarlo.png',format='png')
print "check .png for graphic demonstration"
