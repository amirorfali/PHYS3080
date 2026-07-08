import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import integrate

# Lets get a theoretical plot using standard equation of z(a)=1/a-1

def redshiftAtScaleFactor(a):
    return (1/a)-1

#Array of scalefactor values

aStart=0.1
aEnd=2.1
aStep=0.05

aVals=np.arange(aStart, aEnd, aStep)

# Populate the scalefactor array
zVals = np.zeros(len(aVals))
zToday = 0

for i, a in enumerate(aVals):
    zVals[i]=redshiftAtScaleFactor(a)
    if (a==1): #Lets plot redshift at our scalefactor
        zToday=zVals[i]


#Plot theoretical values
plt.plot(zVals,aVals)
plt.xlabel('Scalefactor Values (a)')
plt.ylabel('Redshift Values (z)')
plt.plot(zToday,1.0,'o')
plt.show()

