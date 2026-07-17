import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import integrate

def EzInv(z):
    return np.sqrt(.31*(1+z)**3+0.69) #Hard code om to 0.31 and ol to 0.69

H0kmsMpc = 70 
c = 299792.458 

zStart = 0.1
zStop = 2.1
zStep = 0.1
redshiftVals = np.arange(zStart, zStop, zStep)

coMovingVals = np.zeros(len(redshiftVals))

for i, z in enumerate(redshiftVals):
    coMovingVals[i] = integrate.quad(EzInv,0,z)[0]*c/H0kmsMpc

plt.plot(redshiftVals, coMovingVals)
plt.xlabel('Redshft (z)')
plt.ylabel('Co-Moving Distanace (Mpc)')
plt.show()
    