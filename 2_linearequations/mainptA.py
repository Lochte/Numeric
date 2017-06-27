from __future__ import division
from QRdecomp import *
import numpy as np

print("###### Task A ######")
A = np.array([[1,4],[2,4],[3,5]])
b = np.array([[9],[5],[9]])

Q,R = QRdec(A)
print("###### Part 1 ######")
print("Matrix A")
print(A)
print("Q matrix of matrix A")
print(Q)
print("R matrix of matrix A")
print(R)
print("Check that QTQ = 1:")
print(np.dot(Q.transpose(),Q))
print("Check that Q * R = A?")
print(np.dot(Q,R))

print("###### Part 2 ######")
A = np.array([[2,3,1],[1,3,4],[1,2,1]])
b = np.array([[7],[15],[22]])

Q,R = QRdec(A)
x   = QRback(Q,R,b)
print("square matrix A:")
print(A)
print("random vector b:")
print(b)
print("Vector x (solution to A * x = b)")
print(x)
print("Check that A * x = b")
print(np.dot(A,x))
