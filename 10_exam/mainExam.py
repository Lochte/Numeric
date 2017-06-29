from __future__ import division
from integrator import *
import numpy as np
import counter
import scipy.integrate as integrate


print '###### Exam ######'
print '\n'

def f(x):
    f = np.cos(x)
    return f
a = -1
b = 1

acc = 1e-3
eps = 1e-3

print 'The integral of cos(x) is found:'
print 'the exact result is:'
result,error=integrate.quad(f,-1,1)
print result

qtype=1              # Choose the correct weights
trans = 1             # Activates Clenshaw Curtis transformation
counter.calls = 0     # resets counter calls
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with clenshaw curtis transformation is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

trans = 0
counter.calls = 0
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with regular adaptive integration is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

print '\n'

print '---------------------------'
def f(x):
    f = x*x
    return f
a = -1
b = 1

acc = 1e-3
eps = 1e-3

print 'The integral of x^2 is found:'
print 'the exact result is:'
result,error=integrate.quad(f,-1,1)
print result

trans = 1             # Activates Clenshaw Curtis transformation
counter.calls = 0     # resets counter calls
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with clenshaw curtis transformation is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

trans = 0
counter.calls = 0
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with regular adaptive integration is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

print '---------------------------'
def f(x):
    f = np.exp(x)
    return f
a = -1
b = 1

acc = 1e-3
eps = 1e-3

print 'The integral of exp(x) is found:'
print 'the exact result is:'
result,error=integrate.quad(f,-1,1)
print result

trans = 1             # Activates Clenshaw Curtis transformation
counter.calls = 0     # resets counter calls
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with clenshaw curtis transformation is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

trans = 0
counter.calls = 0
Qo=adapt(f,a,b,acc,eps,qtype,trans)
print '\n'
print 'The calculated integral with regular adaptive integration is:\n',Qo
print '# of integrand calls:', counter.calls
print '\n'

print 'it seems the two methods are compareable in efficiency..'
