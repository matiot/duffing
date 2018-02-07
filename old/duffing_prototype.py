import numpy as np
import math
from rungekutta import *
import matplotlib.pyplot as plt

def make_g_fun(a,b,c):
    return lambda y,t: np.array([ y[1], a*y[1]-b*y[0] - c*y[0]**3 ])


def g(y,t):
    # y1 = [ 0, 0 ]
    # y1[0] = y[1]
    # y1[1] = -y[0] #+ y[0]**3
    return np.array([ y[1], -1*y[1]-2*y[0] - 3*y[0]**3 ])

def graph(data):
    plt.clf()
    t = []
    y = []
    v = []
    for i in range(len(data)):
        t.append(data[i][0])
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    plt.plot(t,y,'r-',label='position')
    plt.plot(t,v,'b.',label='velocity')
    plt.xlabel(r'$2\pi t/T$')
    plt.legend(loc=1)
    plt.show()
    return

y = np.zeros(2)
y[0] = 1.
y[1] = 1.

function = make_g_fun(0,2,0)
print(g(y,0))
print(function(y,0))

t = 0.
dt = 0.1
n = 1000


dat = rk(function, y, t, dt, n)

graph(dat)
