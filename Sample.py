#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:00:47 2022

@author: anubhabal
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math
import pandas as pd
#Amplitdue vs Frequency for R=1

F1=pd.read_excel('Downloads/ICL Computing/Year 1 Computing/AmplitudeData.xlsx', usecols="A",skiprows=2, nrows=21)
#print(F1)
A1=pd.read_excel('Downloads/ICL Computing/Year 1 Computing/AmplitudeData.xlsx', usecols="B",skiprows=2, nrows=21)
#print(A1)
errorsA1=pd.read_excel('Downloads/ICL Computing/Year 1 Computing/AmplitudeData.xlsx', usecols="C",skiprows=2, nrows=21)
#print(errorsA1)

x=F1[5000].to_numpy()*2*math.pi/100000
y=A1[0.0667].to_numpy()
yerror=errorsA1[0.00266].to_numpy
domain = np.array([i/100 for i in range(35,150)])

import math
from scipy.optimize import curve_fit
def amplitudefunction(x,N,w_0, gamma):
    return N/(((((x**2)-(w_0**2))**2)+((gamma*x)**2))**0.5)
  
guess_N = 0.01
guess_w_0 = 0.17500*2*math.pi
guess_gamma=1000.0

p_0=[guess_N,guess_w_0,guess_gamma]

fit, cov = curve_fit(amplitudefunction, list(x), list(y), p0=p_0, maxfev = 100000)



print('The fit parameters are: ',fit[0],fit[1],fit[2])
data_fit = amplitudefunction(x,fit[0], fit[1],fit[2])


plt.scatter(x,y,c='orange') #scatter vs plot, scatter =points
plt.title('Amplitude vs Frequency for R=1')
plt.ylabel('Amplitude of Signal (V)')
plt.xlabel('w(10^5radians per second)')
plt.plot(domain,amplitudefunction(domain,fit[0], fit[1],fit[2]))
plt.errorbar(x,y,yerr=yerror,fmt="o", capsize=5, elinewidth=0.1)
plt.legend()
plt.grid()
plt.show()
errors=list(errorsA1[0.00266].to_numpy())
plt.errorbar(x,y,yerr=errors,fmt="x", capsize=1, elinewidth=0.1)
plt.legend(["Curve Fit","Points"])
plt.grid()
plt.show()