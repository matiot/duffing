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
y[0] = 0.
y[1] = 1.

#simulation window
t = 0.
dt = 0.1
n = 100

#open graph
graph = PdfPages('data/pdfgraphs.pdf')
AC = [ 0., 0.2, 0.8, 1., 2., 10. ]
BB = [ -10., -2., -1., 0. ]

for A in ABC:
    for C in ABC:
        plt.clf()
        plt.title('A='+str(round(A,1))+' C='+str(round(C,1)))
        for B in BB:
            print(A,B,C)
            g = duffing.make_g_duffing(A,B,C)
            dat = rungekutta.rungekutta(g, y, t, dt, n)
            # filename = 'data/scanbyParam/Param_'+str(round(A,1))+'_'+str(round(B,1))+'_'+str(round(C,1))+'.dat'
            # print(filename)
            # np.savetxt(filename, dat)
            plt.plot(dat[:,1],dat[:,2],'-',label='B='+str(round(B,1)))
            xeq = [ 0. ]
            yeq = [ 0. ]
            if B < 0.:
                xeq.append(-np.sqrt(-1./B))
                xeq.append(np.sqrt(-1./B))
                yeq.append(0.)
                yeq.append(0.)
            plt.plot(xeq,yeq,'x')
            plt.legend(loc=1)
            
        graph.savefig()
            
graph.close()



