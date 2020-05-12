# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:44:04 2020

@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
import random as rd
from scipy import interpolate

############# Recamans Sequence ##################
# The rules of the Recamans sequence are:
# Start at 0
# Each term in the sequence must be > 0
# At each step you move backwards if possible otherwise move forwards
# Cannot repeat an item that is already in the sequence 

# Example: Starting at 0 and step = 1, going backwards give us a value of -1
#          so we have to move forward giving us a value of 1.
#          Now for step = 2, going backwards from 1 gives us a value of -1 so
#          we move forward to 3.


# Define Recaman Sequence
def Recamans_Sequence(iterations):
    array = np.zeros((1,iterations), dtype = int)
    for i in range(0,iterations):
        if i == 0:
            array[0][i] = 0
            step = 1
            value = 0
        elif value - step > 0 and value - step not in [array[0][j] for j in range(0,i)]:
            value = value -  step
            step = step + 1
            array[0][i] = value 
        else:
            value = value + step 
            step = step + 1
            array[0][i] = value 
    return array


Recamans_Sequence = Recamans_Sequence(500)
x = np.arange(0,Recamans_Sequence.size, 1).reshape(1,500)


# Plot Recamans Sequence 
plt.figure()
plt.plot(x, Recamans_Sequence, 'bx')
plt.show()


# Plot Recamans sequence with curve fitting
x = np.reshape(x,(500,))
Recamans_Sequence = np.reshape(Recamans_Sequence, (500,))

f = interpolate.interp1d(x, Recamans_Sequence)
xnew = np.arange(0,498, 0.1)
ynew = f(xnew)
plt.figure(figsize = (10,5))
plt.plot(x, Recamans_Sequence, 'o', xnew, f(xnew), '-')
plt.xlim(0,500)
plt.show()

















