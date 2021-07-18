import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, axes
from scipy import optimize
import numpy as np

def fit_func(x, a, b):
  return (a*x+b)
  
def plotter(matrix, dim, x, fit, outfile, outdir):
     num=0
     plt.clf()
     palette = plt.get_cmap('hsv')

     for rows in range(0,matrix.shape[dim]):
       h_pre = plt.figure(31)
       num+=1
       
       if dim==0:
            plt.plot(x, matrix[rows,:], marker='', color=palette(num), linewidth=1, alpha=0.9, label=rows)
       else:
            plt.plot(x, matrix[:,rows], marker='', color=palette(num), linewidth=1, alpha=0.9, label=rows)

#plt.legend(loc=2, ncol=2)   
#       plt.xlabel('x(units)',fontsize=16)
#       plt.ylabel('Intensity(units)',fontsize=16)
     
       plt.savefig(outdir+"/"+outfile+"_"+str(num))
       plt.clf()
     
       h_pre.show()  
       
       
def plotter_Fit(matrix, dim, x, fit, outfile, outdir):
     list_m_fit = []
     palette = plt.get_cmap('hsv')
     plt.clf()
     num=0
     x=x*0.154 #from pixel to um
     x = x/np.max(x) #x goes from 0 to 1 
     print "\nFitting procedure"
     for rows in range(0,matrix.shape[dim]):
       
       h = plt.figure(3)
       num+=1
       
       plt.plot(x, matrix[rows,:]/np.max(matrix[rows,:]), marker='', color=palette(num), linewidth=1, alpha=0.9, label=rows)
       params, params_covariance = optimize.curve_fit(fit_func, x, matrix[rows,:]/np.max(matrix[rows,:]), bounds=((-np.inf, -np.inf), (np.inf,np.inf)))
       
       

    
 #      plt.plot(x, matrix[rows,:]), marker='', color=palette(num), linewidth=1, alpha=0.9, label=rows)
 #      params, params_covariance = optimize.curve_fit(fit_func, x, matrix[rows,:], bounds=((-np.inf, -np.inf), (np.inf,np.inf)))
       plt.plot(x,fit_func(x, params[0], params[1]), label='Fit')
       # text(0.5, 0.5, str(params[0]), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)     #plt.legend(loc=2, ncol=2)
       plt.xlabel('x(units)',fontsize=16)
       plt.ylabel('Intensity(units)',fontsize=16)
     
       plt.savefig(outdir+"/"+outfile+"_"+str(num))
       list_m_fit.append(params[0])
       plt.clf()
     
       h.show()
       
     return list_m_fit