# pands-problem-set
First Assessment

This is the first assessment for the Programming and Scripting Module of the H.Dip Data Analytics, First Semester. This Assessment is worth 50% of the total marks for this module.

Built with Python 3.7.1, Visual Studio Code 1.32.3, Anaconda 1.9.6

Problem 1 - "Sumupto.py" is for the purpose of summing all integers between user inputted number and 1. This requires the user to input a positive integer after the program is ran, to get an output. It features an 'if' function to stop the user inputting a integer that is negative and an 'elif' function, to encourage the user to input an integer larger that 1.

Problem 2 - "begins-with-t.py" is for the purposes of outputting whether or not 'today' is a day that begins with the letter 'T'. It features the use of the 'datetime' function and 'string format time' (strftime). The resultant output with confirm if the current date does or does not begin with the letter 'T' with the use of a simple if statement.

Problem 3 - "divisors.py" is for the purposes of printing all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. It makes use of an empty number list that is populated with numbers that are checked sequencially, and added to the list that pass the 'test'. This is then printed at the end.

Problem 4 - "collatz.py" is based off the famous Collatz conjecture. In this the user will input any positive integer and the program will output the successive values of collatz calculation. in the collatz calculation, at each step, the program will calculate the next value by taking the current value and, if it is even, divide it by two; if the number is odd, multiple it by three and add one. Ultimately, regardless of what positive integer is input, the program will always reach 1.

Problem 5 - "primes.py" is for the purposes of informing the user if the user-input number is a prime or not. This program uses a range function, if the input number is ever divisable with no remainder by any number, between 2 and the user-input number itself, it is not prime. 

Problem 6- "secondstring.py" is a program that takes a user input string and outputs every second word. This program uses the split and join functions to split the string and rejoin it with the alternate words in a new string.

Problem 7 - "squareroot.py" is a program that that takes a positive floating point number as input and outputs an approximation of its square root. it utilises the 'Math' module and 'sqrt' function. The resultant output is formatted to 3 DP.

Problem 8 "datetime1.py" is a program that outputs today’s date and time in the format "Monday, January 10th 2019 at 1:15pm". It requires no user input, other than to run the program. It features a datetime module and string format time.

Problem 9 "secondline.py" is a program that reads in a text file and outputs every second line. The program takes the filename from an argument on the command line. The program uses the 'sys' module and sys.argv to read the input file, found the the current working folder, and prints every other line in the entire file. "testfile.txt" and "mobydick.txt" have been included, "testfile.txt" is very small, with only 10 lines, "mobydick.txt" is the full Moby Dick book, significantly long.

Problem 10 "plotting.py" is a  program that displays a plot of the functions x, x2 and 2x in the range [0, 4]. It utilises 'numpy' and 'matplotlib.pyplot' modules to create 'arange' and plot the output of the functions. 

