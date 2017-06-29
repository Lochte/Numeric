import matplotlib.pyplot as plt
import numpy as np
import linearinterpolation as inter
import quadraticspline as qinter
np.seterr(divide='ignore', invalid='ignore')

data = np.loadtxt('testdat.txt')

x = data[:,0]
y = data[:,1]
z = np.linspace(x[0],len(x),100000)
plt.plot(x,y,'bo',label='Given points')

# linear spline interpolation
f1 = inter.linterp(x,y,z)
plt.plot(z,f1,label='Linear interpolation')

# quadratic spline interpolation
f2,qint,dint = qinter.qinterp(x,y,z)
plt.plot(z,f2,label='Quadratic interpolation')
plt.plot(z,qint,label='Quadratic integration accumulated')
plt.plot(z,dint,label='Quadratic differentiation')

# move legend to upper left, add shadows
legend = plt.legend(loc='upper left', shadow=True, fontsize='large')

# saving figure
plt.savefig('linearandquad.png',format='png')
