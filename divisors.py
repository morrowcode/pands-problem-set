# Problem 3 - program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# Colin Morrow 27/02/2019

#empty nmber list to be populated with numbers that pass the 'test'
numl = []

#numbers that are to be used 1,000 to 10,000
for i in range(1000, 10000):
    
    # testing for division by 6 then by 12 - using % as modulo - 0 remainder means divides perfectly - if true, appended to empty number list 
    if (i % 6 == 0) and (i % 12 != 0):
        
        # Empty number list with appended numbers that pass 'test' - in string format
        numl.append(str(i))
#Printing number list seperated by comma
print(', ' .join (numl))