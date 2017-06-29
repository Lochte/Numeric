import matplotlib.pyplot as plt
import numpy as np
import linearinterpolation as linearinterpolation

Data = np.loadtxt('testdat.txt')

x = Data[:,0]
y = Data[:,1]
z = np.linspace(x[0],len(x),100)

plt.plot(x,y,'bo',label='Given points')


# linear interpolation
f1 = linearinterpolation.linterp(x,y,z)
plt.plot(z,f1, label = 'Linear interpolation')

legend = plt.legend(loc='upper left', shadow=True, fontsize='large')

plt.savefig('linear.png',format='png')
