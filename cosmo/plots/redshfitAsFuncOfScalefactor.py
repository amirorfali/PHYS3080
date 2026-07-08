import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import integrate

# Lets get a theoretical plot using standard equation of z(a)=1/a-1

def redshiftAtScaleFactor(a):
    return (1/a)-1

#Array of scalefactor values
aStart=0.5
aEnd=2.1
aStep=0.01

aVals=np.arange(aStart, aEnd, aStep)


# Populate the scalefactor array
zVals = np.zeros(len(aVals))
zToday = 0

for i, a in enumerate(aVals):
    zVals[i]=redshiftAtScaleFactor(a)
    if (a==1): #Lets plot redshift at our scalefactor
        zToday=zVals[i]




#We have data for 1635 supernovas and their reshifts, if we take the avergae between zCMB, zHD, and zHEL, we could probably
#find realistic scalefactor values that should align with our theoretical values

def readData(modelName):
    d = np.genfromtxt('cosmo/docs/notebooks/data/'+modelName+'.csv',delimiter=',', skip_header=1)
    zCMB = d[:,2]
    zHD = d[:,3]
    zHEL = d[:,4]

    return (zCMB+zHD+zHEL)/3

zValsData = readData('DES-SN5YR_HD')

aValsData = np.zeros(len(zValsData))

for i, zVal in enumerate(zValsData):
    aValsData[i] = 1/(1+zVal)

#Plot theoretical and actual values
plt.plot(aVals,zVals,'-.', color='red')
plt.plot(aValsData,zValsData, color='blue')
plt.xlabel('Scalefactor Values (a)')
plt.ylabel('Redshift Values (z)')

plt.plot(1.0, zToday, 'o')
plt.show()

#It appears that the actual data does follow the exponetial decay trend of the the redshift as scalefactor increases
#This was expected and makes sense as the smaller and more dense our universe was, the older it was, and therefore the more strectjed the light should be
#I can imporve upon this via measuring how good the data fits the equation z=(1/a)-1 
#This can be done via calculating the chi2, delta chi2, and reduced chi2




