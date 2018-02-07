import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization
import os
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

#touch data/ folder if npn-existent
if not os.path.exists('data/scanbyParam'):
    os.makedirs('data/scanbyParam')

#initìial data
y = np.zeros(2)
y[0] = 1.
y[1] = 1.

#simulation window
t = 0.
dt = 0.1
n = 10

#open graph
# graph = PdfPages('data/pdfgraphs.pdf')

for A in np.arange(0,10):
    for B in np.arange(0,10):
        for C in np.arange(0,10):
            g = duffing.make_g_duffing(A,B,C)
            dat = rungekutta.rungekutta(g, y, t, dt, n)
            filename = 'data/scanbyParam/Param_'+str(A)+'_'+str(B)+'_'+str(C)+'.dat'
            print(filename)
            np.savetxt(filename, dat)

            # plt.clf()
            # plt.plot(dat[:,1],dat[:,2])
            # plt.title('A='+str(A)+' B='+str(B)+' C='+str(C))
            # graph.savefig()

# graph.close()



