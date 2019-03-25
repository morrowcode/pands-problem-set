#Write a program that that takes a positive floating point number as input and outputs
#an approximation of its square root.
#Colin Morrow
#25/03/2019

#Calling Math module
import math

#User input - Float to allow decimals
i = float (input("Please enter a positive number:"))

#defining j variable as the square root of the user input 'i' variable
j = math.sqrt(i)

#printing out 'i' and 'j' to 3 decimal places.
print('The square root of %.3F is approx. %.3f'%(i, j))
