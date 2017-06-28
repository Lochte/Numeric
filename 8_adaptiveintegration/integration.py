from __future__ import division
import numpy as np
import sys
import counter

inf=float("inf")


def adapt(f,a,b,acc,eps,qtype):
	if qtype==0:
		x = np.array([0.,2/6,4/6,1.])
	else:
		x = np.array([1/6,2/6,4/6,5/6])
	n = len(x)
	h = (b - a)
	fn=np.zeros(n)

	if a==-inf and b==inf:
		f_ny=f
		a=0.
		b=1.
		h = (b - a)
		def g(x):
			g = (f_ny((1-x)/x)+f_ny((x-1)/x))/(x*x)
			return g
		for i in range(n):
			fn[i] = g(a + h * x[i])
	elif a!=inf and b==inf:
		f_ny=f
		a_ny=a
		a=0.
		b=1.
		def g(x):
			g = (f_ny(a_ny+(1-x)/x))/(x*x)
			return g
		for i in range(n):
			fn[i] = g(a + h * x[i])
	elif a==-inf and b!=inf:
		f_ny=f
		b_ny=b
		a=0.
		b=1.
		def g(x):
			g = (f_ny(b_ny-(1-x)/x))/(x*x)
			return g
		for i in range(n):
			fn[i] = g(a + h * x[i])
	else:
		for i in range(n):
			fn[i] = f(a + h * x[i])
	return quadratic(x,f,fn,a,b,acc,eps,qtype)

def quadratic(x,f,fn,a,b,acc,eps,qtype):
	if qtype==0:
		w = [1/8,3/8,3/8,1/8]

	else:
		w = [2/6,1/6,1/6,2/6]
	v = [1/4,1/4,1/4,1/4]
	Q=0
	q=0
	h=b-a
	n=len(w)

	for i in range(n):
		Q+=(w[i]*fn[i])*h
		q+=(v[i]*fn[i])*h
	err=np.absolute(Q-q)
	counter.calls += 1
	if err<(acc+np.absolute(Q)*eps):
		return Q, err
	else:
		acc=acc/np.sqrt(2)
		mid=(a+b)/2
		Qleft,errl=quadratic(x,f,fn,a,mid,acc,eps,qtype)
		Qright,errr=quadratic(x,f,fn,mid,b,acc,eps,qtype)
		Qtot=Qleft+Qright
		errtot=np.sqrt(errl*errl + errr*errr)
		return Qtot,errtot
