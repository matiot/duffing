import numpy as np
import math

def make_g_duffing(A,B,C):
	return lambda y,t: np.array([ y[1], -2*A*y[1] - y[0] - B*y[0]**3 + np.sin(C*t)])


# Examples...
def g_simple_oscillator(y,t):
	return np.array([ y[1], -y[0] ])

def g_damped_oscillator(y,t):
	return np.array([ y[1], -2*y[0] -y[1]])

def g_free_duffing(y,t):
	return np.array([ y[1], -2*y[1] - y[0] - y[0]**3 ])

def g_forced_duffing(y,t):
	return np.array([ y[1], -2*y[1] - y[0] - y[0]**3 ] + np.cos(t))
