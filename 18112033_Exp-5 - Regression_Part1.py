# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:33:58 2021

@author: Jeet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#Creating the dataframe
data = {'Temperature':[-36.7,-19.6,-11.5,-2.6,7.6,15.4,26.1,42.2,60.6,80.1],
        'Pressure':[1,5,10,20,40,60,100,200,400,760]}
df = pd.DataFrame(data)

'''Degree 2 Polynomial Fitting'''
polymodel = np.poly1d(np.polyfit(df.Temperature, df.Pressure, 2))
polyline = np.linspace(-60, 100)
plt.figure()
plt.scatter(df.Temperature, df.Pressure)
plt.plot(polyline, polymodel(polyline))
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title("Polynomial fit of degree 2")
plt.show()

print('R2 score of degree 2 fit is ',r2_score(df.Pressure, polymodel(df.Temperature)))

'''Degree 3 Polynomial Fitting'''
polymodel = np.poly1d(np.polyfit(df.Temperature, df.Pressure, 3))
polyline = np.linspace(-60, 100)
plt.figure()
plt.scatter(df.Temperature, df.Pressure)
plt.plot(polyline, polymodel(polyline))
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title("Polynomial fit of degree 3")
plt.show()

print('R2 score of degree 3 fit is ',r2_score(df.Pressure, polymodel(df.Temperature)))

'''Degree 4 polynomial Fitting'''
polymodel = np.poly1d(np.polyfit(df.Temperature, df.Pressure, 4))
polyline = np.linspace(-60, 100)
plt.figure()
plt.scatter(df.Temperature, df.Pressure)
plt.plot(polyline, polymodel(polyline))
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title("Polynomial fit of degree 4")
plt.show()

print('R2 score of degree 4 fit is ',r2_score(df.Pressure, polymodel(df.Temperature)))

'''Use scipy based fitting if you want the equation primarily'''
#from scipy.optimize import curve_fit
#def linear_function(x, a, b):
#    return a * x + b
#def quadratic_function(x, a, b, c):
#    return a * x**2 + b * x + c
#def cubic_function(x, a, b, c, d):
#    return a * x**3 + b * x**2 + c * x + d
#def degreefourpoly(x, a, b, c, d, e):
#    return a * x**4 + b * x**3 + c * x**2 + d * x + e

#m = curve_fit(linear_function, df.Temperature, df.Pressure)[0]
#n = curve_fit(quadratic_function, df.Temperature, df.Pressure)[0]
#o = curve_fit(cubic_function, df.Temperature, df.Pressure)[0]
#p = curve_fit(degreefourpoly, df.Temperature, df.Pressure)[0]


