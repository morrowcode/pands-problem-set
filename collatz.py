#Problem 4 - input any positive integer and will output the successive values of collatz calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two. 
# If the number is odd, multiple it by three and add one
#Colin Morrow  01/03/2019

#defining the loop
def collatz(number):
    
    #if its even
    if number % 2 == 0:
        #print the result
        print(number // 2)
        #number now divided by 2
        return number // 2
    #If the number is odd
    else:
        #defining the sum for an odd number for printing
        odd = (number * 3 + 1)
        print(odd)
        #number is times by 3 and 1 added
        return number * 3 + 1

#user data entry for start point
n = int(input("Enter a postive integer..."))
#define the end point for the sequence - while not 1

while (n != 1):
    n = collatz(int(n))
