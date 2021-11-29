# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:57:34 2021

@author: Jeet
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution

d1 = np.array([85.47,90,100,110,120,130,140,150,160,170,180,190,200,210,220,231.07,240,250,260,270,280,290,300,310,320,330,340,350,360])
d2 = np.array([0.000169,0.000969,0.0251,0.34511,2.948,17.534,78.671,282.35,847,2200,5050,10500,20100,35900,60500,101000,148000,218000,311000,430000,582000,769000,998000,1270000,1600000,1980000,2430000,2950000,3550000])
xdata = d1-273.15
ydata = d2/133
df = pd.DataFrame({'Temperature': xdata, 'Pressure': ydata})

def func(T,A,B,C):
    y = 10**(A + (B / ( T + C)))
    return y

def sumofsqerr(parameterTuple):
    val = func(xdata, *parameterTuple)
    return np.sum((ydata - val) ** 2.0)

def generate_Initial_Parameters():
    parameterBounds = []
    parameterBounds.append([3.0, 11.0]) # search bounds for A
    parameterBounds.append([900.0, 3000.0]) # search bounds for B
    parameterBounds.append([200.0, 400.0]) # search bounds for C
    result = differential_evolution(sumofsqerr, parameterBounds, seed=3)
    return result.x

geneticPara = generate_Initial_Parameters()

fpara, pcov = curve_fit(func, xdata, ydata, geneticPara)
print('Fitted parameters:', fpara)

modelPredictions = func(xdata, *fpara)
absError = modelPredictions - ydata

Rsquared = 1.0 - (np.var(absError) / np.var(ydata))
print('R-squared:', Rsquared)

plt.scatter(xdata, ydata)
plt.plot(xdata, func(xdata, *fpara), 'r')
plt.show()


