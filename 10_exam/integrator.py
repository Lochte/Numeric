from __future__ import division
import numpy as np
import sys
import counter

inf=float("inf")

def fn(a,b,x):
	return a + (b-a)*x



def adapt(g,a,b,acc,eps,qtype,trans):
	if qtype==0:
		x = np.array([0.,2/6,4/6,1.])
	else:
		x = np.array([1/8,3/8,5/8,7/8])
	n = len(x)
	h = (b-a)
	fm=np.zeros(n)

	if a==-inf and b==inf:
		f_ny=g
		a=0.
		b=1.
		h = (b - a)
		def g(x):
			g = (f_ny((1-x)/x)+f_ny((x-1)/x))/(x*x)
			return g
		for i in range(n):
			fm[i] = g(fn(a,b,x[i]))
	elif a!=inf and b==inf:
		f_ny=f
		a_ny=a
		a=0.
		b=1.
		def g(x):
			g = (f_ny(a_ny+(1-x)/x))/(x*x)
			return g
		for i in range(n):
			fm[i] = g(fn(a,b,x[i]))
	elif a==-inf and b!=inf:
		f_ny=f
		b_ny=bcd
		a=0.
		b=1.
		def g(x):
			g = (f_ny(b_ny-(1-x)/x))/(x*x)
			return g
		for i in range(n):
			fm[i] = g(fn(a,b,x[i]))
	elif a==-1 and b==1 and trans==1:       # Clenshaw curtis conditions
		f_ny=g                            	# old function is stored in f_ny
		a = 0                               # lower limit is changed to 0
		b = np.pi                           # upper limit is changed to pi
		h = (b - a)
		def g(x):
			g = (f_ny(np.cos(x))*np.sin(x)) # Clenshaw curtis transformation
			return g
		for i in range(n):
			fm[i] = g(fn(a,b,x[i]))
	else:
		for i in range(n):
			fm[i] = g(a + h * x[i])
	return quadratic(x,g,fm[2],fm[3],a,b,acc,eps,qtype)

def quadratic(x,f,f2,f3,a,b,acc,eps,qtype):
	w = [2/6,1/6,1/6,2/6]
	v = [1/4,1/4,1/4,1/4]
	Q=0
	q=0
	h=b-a
	n=len(w)

	f1 = f(fn(a,b,x[0]))
	f4 = f(fn(a,b,x[3]))
	fall = [f1, f2, f3, f4]
	for i in range(n):
		Q+=(w[i]*fall[i])*h
		q+=(v[i]*fall[i])*h
	err=np.absolute(Q-q)
	counter.calls += 1
	if err < (acc+np.absolute(Q)*eps):
		return Q
	else:
		acc=acc/np.sqrt(2)
		mid=(a+b)/2
		return quadratic(x,f,f1,f2,a,mid,acc,eps,qtype)+quadratic(x,f,f3,f4,mid,b,acc,eps,qtype)
