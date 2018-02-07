import numpy as np


def rk_step(g, y0, t0, dt):
	"""Execute a Runge-Kutta step

	Keyword arguments:
	g -- integrand function
	y0 -- (list) initial data
	t0 -- (float) initial time
	dt -- (float) time step

	Return :
	y1 -- list of components of the function at time t1
	"""
	c1 = g(y0        , t0        )*dt
	c2 = g(y0 + c1/2., t0 + dt/2.)*dt
	c3 = g(y0 + c2/2., t0 + dt/2.)*dt
	c4 = g(y0 + c3   , t0 + dt   )*dt
	return y0 + 1./6.*( c1 + 2.*c2 + 2.*c3 + c4 )


def euler_step(g, y0, t0, dt):
	"""Execute an Euler step

	Keyword arguments:
	g -- integrand function
	y0 -- (list) initial data
	t0 -- (float) initial time
	dt -- (float) time step

	Return :
	y1 -- list of components of the function at time t1
	"""
	return y0 + g(y0, t0)*dt


def rk(g, y0, t0, dt, n):
	"""Execute a complete Runge-Kutta simultation for n step

	Keyword arguments:
	g -- integrand function
	y0 -- (list) initial data
	t0 -- (float) initial time
	dt -- (float) time step
	n -- (integer) number of time steps
	Return:
	data -- list of tuple (ti=instant time, yy= list of components of the function at time ti)
	"""
	data = [ [t0, y0] ]
	for i in range(1,n):
		ti,yi = data[i-1]
		data.append( [ti + dt, rk_step(g, yi, ti, dt)] )
	return data


def rk_reshape(data):
	"""Transform the data data structure in a numpy matrix
	Warning: it's a sketch. it's only compatible with two values functions (list of two elements)
	Keyword arguments:
	data -- data -- list of tuple (float, list of floats)

	Return:
	data -- matrix of ...
	"""
	t = []
	y = []
	v = []
	for i in range(len(data)):
		t.append(data[i][0])
		y.append(data[i][1][0])
		v.append(data[i][1][1])
	return np.array([ t, y, v ])

def rungekutta(g, y0, t0, dt, n):
	"""Execute a complete Runge-Kutta simultation for n step

	Keyword arguments:
	g -- integrand function
	y0 -- (list) initial data
	t0 -- (float) initial time
	dt -- (float) time step
	n -- (integer) number of time steps

	Return:
	data -- numpy matrix
	"""
	return rk_reshape( rk(g, y0, t0, dt, n) )
