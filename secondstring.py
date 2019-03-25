#Write a program that takes a user input string and outputs every second word.
#Colin Morrow
#24/03/2019

#For the user input
i = input("Please enter a sentence:")

#Splitting function of i (the user input) to create variable j, no start or end required, 
j = i.split()[::2]

#k variable for join function to join string 
k = ' '.join(j)

#Printing output
print(k)
