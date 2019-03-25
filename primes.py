# Problem 5 - Program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime

# Colin Morrow 02/03/2019
n = int(input("Enter a positive integer..."))

if n > 1:

    for i in range(2,n):
        if (n % i) == 0:
            print(n,"is not a prime number")
            print(i,"times",n//i,"is",n)
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is a prime number")