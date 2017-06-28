from __future__ import division
from integration import *
import numpy as np
import counter
import scipy.integrate as integrate

print '###### Task B ###### \n'

print 'The integral calculated is of f(x) = 1/(1+x^2):'

print 'Exact result:\n',np.pi

def f(x):
	f=1/(1+np.power(x,2))
	return f

a=-np.inf
b=np.inf
acc=1e-3
eps=1e-3

qtype=1
counter.calls=0
Qo,erroro=adapt(f,a,b,acc,eps,qtype)
print '\n'
print 'The open sets integral is:\n',Qo
print '# of integrand calls:', counter.calls

print '\n'
print 'scipy.integrate package:'
print 'integration result:'
print integrate.quad(f,-np.inf,np.inf)
