import numpy as np
import counter
import sys
from equations import *
import sys
sys.path.append('/Users/AndersLochte/Documents/numerical/2_linearequations')
from givens import *
import numpy.linalg as LA



def newtonmini(f, xo, gradf, Hess):
	alpha=1e-5
	eps=1e-10
	x=np.copy(xo)
	n=len(x)
	fx=f(x)
	gf=gradf(x)
	H=np.zeros((n,n))
	while True:
		counter.calls +=1
		H=Hess(x)
		Givens(H)
		Dx = -gf
		solve(H,Dx)
		lamb=2.0
		dot=np.dot(gf,Dx)
		while True:
			lamb /= 2.
			y = x+Dx*lamb
			fy = f(y)
			if(fy < fx+alpha*lamb*dot or lamb < 0.002):
				break
		x = y
		fx = fy
		gf = gradf(x)
		if(LA.norm(gf) < eps):
			break
	return x

def quasinewton(f, xo, gradf):
	alpha=1e-5
	eps=1e-3
	x=np.copy(xo)
	n=len(x)

	H_inverse = np.identity(n)
	dfdx=gradf(x)

	while True:
		fx=f(x)
		counter.calls +=1
		Dx = -np.dot(H_inverse,dfdx)
		s = Dx*2

		while True:
			s /= 2.
			z = x + s
			fz = f(z)
			if abs(fz) < abs(fx) + alpha * np.dot(s,dfdx):
				break
			if(LA.norm(s) < 1e-6):
				H_inverse = np.identity(n)
				break

		dfdx_z = gradf(z)
		y = dfdx_z-dfdx
		if abs(np.dot(np.dot(np.transpose(y), H_inverse), s)) < 1e-6:
			H_inverse = np.identity(n)
			break
		else:
			H_inverse += (np.dot(np.dot(s - np.dot(H_inverse,y), np.transpose(s)), H_inverse)) / (np.dot(np.dot(np.transpose(y), H_inverse), s)) #Broyden

		x = z
		fx = fz
		dfdx = dfdx_z

		if (np.linalg.norm(Dx) < 1e-6 or np.linalg.norm(dfdx) < eps):
			break

	return x
