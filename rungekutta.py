import numpy as np


def rk_step(g, y0, t0, dt):
    c1 = g(y0        , t0        )*dt
    c2 = g(y0 + c1/2., t0 + dt/2.)*dt
    c3 = g(y0 + c2/2., t0 + dt/2.)*dt
    c4 = g(y0 + c3   , t0 + dt   )*dt
    return y0 + 1./6.*( c1 + 2.*c2 + 2.*c3 + c4 )


def euler_step(g, y0, t0, dt):
    return y0 + g(y0, t0)*dt


def rk(g, y0, t0, dt, n):
    data = [ [t0, y0] ]
    for i in range(1,n):
        ti,yi = data[i-1]
        data.append( [ti + dt, rk_step(g, yi, ti, dt)] )
    return data


def phase(data):
    y = []
    v = []
    for i in range(len(data)):
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    return np.array([ y, v ])
