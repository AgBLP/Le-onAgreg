# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:46:21 2023

@author: Brendan
"""

import matplotlib.pyplot as plt
import numpy as np

def derive_theta (lambda_0,p,a) :
    res = []
    for k in range (len(lambda_0)):
        res.append((p*lambda_0[k]*np.pi/180)/(a*np.sqrt(1-(p*lambda_0[k]/a)**2)))
    return(res)

a = 1/(500e-6)   # réseau de 500 traits/mm
lambda_0 = np.arange(400,801,1)
p=1             # ordre 1

y = derive_theta(lambda_0, p, a)

plt.plot(lambda_0,y, '-')
plt.xlabel(r'$\lambda$ (en nm)', fontsize = 16)
plt.ylabel(r'$\frac{d\theta_p}{d\lambda}$ (en$\degree.nm^{-1}$)', fontsize = 16)
