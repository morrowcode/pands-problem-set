# Problem 1 - Summing all integers between user inputted number and 1
# Colin Morrow - Wed 27/02/2018

# Asking the user to input a number to define "n"
n = int(input("Enter a positive integer..."))
# total is a reference point for the addition of each integer
total = 0
#need a way of stopping the script at this point as 0 or less isnt positive then we can just have the text output
if n <= 0:

    print("Not really the positive integer I was looking for...")
# the sum of 1 is 1 so id comment here to say something about wanting a bigger number to see what this thing can do
elif n == 1:

    print("You should try a bigger number")
#taken from the loops video
while n > 0:
    #total is for the rolling total of integers between 0 and the user input one
    total = total + n
    n = n - 1

print (total)