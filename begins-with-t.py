# Problem 2 - Outputs whether or not today is a day that begins with the letter T
# Colin Morrow - 27/02/2019

#date and time info imported
from datetime import date

#to set when it is
now = date.today()

#to define the day of the week as the word
day = now.strftime ("%A")

# To choose what letter to query
tdat = ("T")

#square brackets for where in the word to look - tdat for what to look for
if day[0] in tdat:
    # Format for changing the letter so it will change the print statement
    print("Yes - today begins with a {}.".format(tdat))
else:
    print("No - today does not begin with a {}.".format(tdat))

#Commented out - used to make sure I'm definately getting day info through
#print (day)