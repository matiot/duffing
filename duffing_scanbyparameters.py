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
y[0] = 0.5
y[1] = 0.05

#simulation window
t = 0.
dt = 0.01
n = 10000

#open graph
graph = PdfPages('data/pdfgraphs.pdf')
AC = [ 0., 0.5, 1., 6. ]
BB = [ -1./6., 0., 0.5, 1., 10. ]

for A in AC:
    for C in AC:
        plt.clf()
        plt.title('A='+str(round(A,1))+' C='+str(round(C,1)))
        plt.xlabel('position y')
        plt.ylabel(r'velocity $\dot{y}$')
        for B in BB:
            print(A,B,C)
            g = duffing.make_g_duffing(A,B,C)
            dat = rungekutta.rungekutta(g, y, t, dt, n)
            # filename = 'data/scanbyParam/Param_'+str(round(A,1))+'_'+str(round(B,1))+'_'+str(round(C,1))+'.dat'
            # print(filename)
            # np.savetxt(filename, dat)
            plt.plot(dat[:,1],dat[:,2],'-',label='B='+str(round(B,1)))
            xeq = [ y[0] ]
            yeq = [ y[1] ]
#            if B < 0.:
#                xeq.append(-np.sqrt(-1./B))
#                xeq.append(np.sqrt(-1./B))
#                yeq.append(0.)
#                yeq.append(0.)
            plt.plot(xeq,yeq,'x')
            plt.legend(loc=1)
            
        graph.savefig()
            
graph.close()



