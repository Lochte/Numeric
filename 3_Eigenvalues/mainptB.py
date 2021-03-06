from __future__ import division
from jacobidiag import *
import numpy as np
import time

print "###### Task B ######"

A    = np.array([[21.0,7.0,6.0],[7.0,8.0,-10.0],[6.0,-10.0,15.0]])
Aorg = np.copy(A)

print Aorg

EigenvalA,EigenvecA,sweeps = valbyval(A,3)


D = np.zeros(np.shape(A))
n = len(EigenvalA)

for i in range(n):
	D[i,i] = EigenvalA[i]

print "\n"
print "Diagonal matrix D containing eigenvalues"
print D
print "number of sweeps: "
print sweeps

print "\n"
print "Orthogonal matrix V consisting of eigenvectors"
print EigenvecA

print "\n"
print "check that A = VDVT:"
print np.dot(np.dot(EigenvecA,D),EigenvecA.transpose())

print "\n"
print "check that VTAV = D"
print np.dot(np.dot(EigenvecA.transpose(),Aorg),EigenvecA)
print "\n"

print "Comparison:"
start_time = time.time()
EigenvalA,EigenvecA,sweeps = jacobidiag(A)
print "Cyclic solved in:", time.time() - start_time, "seconds"
start_time2 = time.time()
EigenvalA,EigenvecA,sweeps = valbyval(A,3)
print "Value-by-value solved in:", time.time() - start_time2, "seconds"
start_time3 = time.time()
EigenvalA,EigenvecA,sweeps = valbyval(A,1)
print"Value-by-value lowest eigenvalue solved in:", time.time() - start_time3, "seconds"
