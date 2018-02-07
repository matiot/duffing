import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization
import os

foldername = 'data/scanbyInitial'
#touch data/ folder if npn-existent
if not os.path.exists(foldername):
    os.makedirs(foldername)

#initìial data
y = np.zeros(2)

#Parameter
A = B = C = 1
print(B)
g = duffing.make_g_duffing(A,B,C)

#simulation window
t = 0.
dt = 0.1
n = 100



for x in np.arange(-1,1,0.25):
    for v in np.arange(-1,1,0.25):
        y[0] = x
        y[1] = v
        dat = rungekutta.rungekutta(g, y, t, dt, n)
        filename = foldername+'/x0_'+str(round(x,3))+'_v0_' +str(round(v,3))+'.dat'
        print(filename)
        np.savetxt(filename, dat)



