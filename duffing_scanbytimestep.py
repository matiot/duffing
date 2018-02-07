import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization
import os

foldername = 'data/scanbyStep'
#touch data/ folder if npn-existent
if not os.path.exists(foldername):
    os.makedirs(foldername)

#initìial data
y = np.zeros(2)
y[0] = 0.
y[1] = 1.

#Parameter
A = B = C = 1
g = duffing.make_g_duffing(A,B,C)

#simulation window
t = 0.
tf = 3



for n in np.arange(10,100):
    dt = (tf-t)/n
    dat = rungekutta.rungekutta(g, y, t, dt, n)
    filename = foldername+'/dt_'+str(round(dt,4))+'.dat'
    print(filename)
    np.savetxt(filename, dat)


