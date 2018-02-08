import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization

    
A = 1.
B = 2.
C = 3.

y0 = np.zeros(2)
t0 = 0.
y0[0] = 0.5
y0[1] = 0.05
dt = 0.01
n = 1000

g = duffing.make_g_duffing(A,B,C)
dat = rungekutta.rungekutta(g, y0, t0, dt, n)

print('making video...')

visualization.anim(dat[:,1:],n,'A='+str(round(A,1))+'_B='+str(round(B,1))+'_C='+str(round(C,1)))

print('...done!')
