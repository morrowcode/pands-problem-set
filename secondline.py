#Write a program that reads in a text file and outputs every second line. The program
#should take the filename from an argument on the command line.

#Colin Morrow
#25/03/2019
#secondline.py 

#For command line arguments 
import sys

#To make sure only one filename, otherwise else statement
if len(sys.argv) != 2:
    print ("You should supply a single filename.")

#to ensure only one filename
else:
    #open and read file from sys.argv as f
    with open(sys.argv[1]) as f:
        #every other line
        for count, l in enumerate (f, start=0):
            if count % 2 == 0:
                print(l)
