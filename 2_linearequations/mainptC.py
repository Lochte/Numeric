from __future__ import division
from QRdecomp import *
from givens import *
import numpy as np
np.seterr(divide='ignore', invalid='ignore')


A = np.array([[2,3,1],[1,3,4],[1,2,9]])
b = np.array([[7],[15],[22]])
Ainv = np.zeros(np.shape(A))
A_orig = np.copy(A)
b_orig = np.copy(b)

AGiv = Givens(A)


print("###### Task C ######")
print("Square matrix A:")
print(A_orig)
print("Vector b")
print(b_orig)

print("Givens rotation of matrix A")
print(AGiv)
print("Solution to A * x = b")
solve(AGiv,b)
print b
print("Check that A * x = b")
print(np.dot(AGiv,b))
