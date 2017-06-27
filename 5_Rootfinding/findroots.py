import numpy as np
from numpy import linalg as LA
import sys
sys.path.append('/Users/AndersLochte/Documents/numerical/2_linearequations')
from givens import *
import rootcounter

global calls

def newtons(f, xo, dx, eps):
	x = np.copy(xo)
	n = len(x)
	A = np.zeros((n,n))
	while True:
		rootcounter.calls += 1
		fx = f(x)
		for j in range(n):
			x[j] += dx[j]
			df = f(x) - fx
			rootcounter.calls += 1
			for i in range(n):
				A[i,j] = df[i]/dx[j]
			x[j] -= dx[j]
		Givens(A)
		Dx = -fx
		solve(A,Dx)
		lamb=2.0
		while True:
			rootcounter.calls += 1
			lamb /= 2
			y = x + Dx * lamb
			fy = f(y)
			if (LA.norm(fy) < (1-lamb/2)*LA.norm(fx) or  lamb < 0.02):
				break
		x = y
		fx = fy
		if( LA.norm(Dx) < LA.norm(dx) or LA.norm(fx) < eps):
			break
	return x

def jacnewtons(f, xo, Jacf, eps):
	x=np.copy(xo)
	n=len(x)
	J=np.zeros((n,n))
	while True:
		fx=f(x)
		rootcounter.calls += 1
		J=Jacf(x)
		rootcounter.calls += 1
		Givens(J)
		Dx = -fx
		solve(J,Dx)
		lamb = 2.0
		while True:
			rootcounter.calls += 1
			lamb /= 2
			y = x + Dx * lamb
			fy = f(y)
			if(LA.norm(fy)<(1-lamb/2)*LA.norm(fx) or  lamb < 0.02):
				break
		x = y
		fx = fy
		if(LA.norm(fx) < eps):
			break
	return x
