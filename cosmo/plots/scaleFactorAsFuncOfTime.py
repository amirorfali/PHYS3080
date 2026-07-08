import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import integrate


c = 299792.458 # km/s (speed of light)

H0kmsmpc = 70.  # Hubble constant in km/s/Mpc
H0s = H0kmsmpc * 3.2408e-20 # H0 in inverse seconds is H0 in km/s/Mpc * (3.2408e-20 Mpc/km)
H0y = H0s * 3.154e7 * 1.e9 # H0 in inverse Giga years is H0 in inverse seconds * (3.154e7 seconds/year) * (1e9 years / Giga year)

#1/H0y would give age of the universe with G is 1x10^9 years

def adotinv(a):
    return np.sqrt(a)

# Make an array of a vals
aStart=0.0
aStop=10
aStep=0.05
aVals=np.arange(aStart, aStop, aStep)

# Make an array for the scalefactor vs time vals
tGyr = np.zeros(len(aVals))

for i, aEnd in enumerate(aVals):
    tGyr[i] = integrate.quad(adotinv,0,aEnd)[0] / H0y

# Plot the data
plt.plot(tGyr,aVals)
#plt.plot(age_Gyr, 1.0,'o') # Put a dot at the current time
#plt.plot(t_analytic_Gyr, a_arr,':',color='red')
plt.xlabel('Time (Gyr)')
plt.ylabel('Scalefactor')
plt.show()
