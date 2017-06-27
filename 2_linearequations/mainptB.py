from __future__ import division
from QRdecomp import *
import numpy as np

print("###### Task B ######")
A = np.array([[2,3,1],[1,3,4],[1,2,1]])
b = np.array([[7],[15],[22]])

Q,R = QRdec(A)
Ainv = QRinverse(Q,R)


print("Square matrix A:")
print(A)
print("inverse B:")
print(Ainv)
print("check that AB = I :")
print(np.dot(A,Ainv))
