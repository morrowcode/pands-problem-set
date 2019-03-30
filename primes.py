# Problem 5 - Program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime

# Colin Morrow 
# 02/03/2019

#User input for checking prime
n = int(input("Enter a positive integer..."))

# 1 is a prime, is its bigger, it goes to 'for' loop
if n > 1:
    #for the range of 2, to the inputted number 
    for i in range(2,n):
        #if the input number is ever divisable with no remainder 
        #by any number, between 2 and the number itself, it is not prime
        if (n % i) == 0:
            print(n,"is not a prime number")
            print(i,"times",n//i,"is",n)
            break
    #...otherwise its a prime number
    else:
        print(n,"is a prime number")
#'else' from top 'if' statement
else:
    print(n,"is a prime number")