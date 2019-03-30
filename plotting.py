#Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].
#Colin Morrow
#30/03/2019

#Import Numpy
import numpy as np
#Import Py plot
import matplotlib.pyplot as plt

#Creating range of [0,4]
x = np.arange(0, 4)

#pyplot for the 3 functions
plt.plot(x, x, 'gs', x, x**2, 'r^', x, 2**x, 'b--')
plt.show()

