import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization
import os
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

foldername = 'data/scanbyStep'
#touch data/ folder if npn-existent
if not os.path.exists(foldername):
    os.makedirs(foldername)

#initìial data
y = np.zeros(2)
y[0] = 0.001
y[1] = 0

#Parameter
A = B = C = 0
g = duffing.make_g_duffing(A,B,C)

#simulation window
t = 0.
tf = np.pi

#initìial data
y = np.zeros(2)
y[0] = 1
y[1] = 0

#simulation window
t = 0.
dt = 0.1
n = 100

nrange = [ 100, 1000, 3000, 10000, 30000 , 100000, 200000]
datapoints = []


plt.clf()
for n in nrange:
    dt = (tf-t)/n
    datapoints.append([dt, np.abs(rungekutta.rungekutta(g, y, t, dt, n)[-1,1]+1)])
    

print(np.matrix(datapoints))
    

plt.plot(np.matrix(datapoints)[:,0],np.matrix(datapoints)[:,1],'o-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('dt')
plt.ylabel('relative error of y at half period')
plt.show()










