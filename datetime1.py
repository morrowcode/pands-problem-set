#Write a program that outputs today’s date and time in the format ”Monday, January
#10th 2019 at 1:15pm”.

#Colin Morrow
#25/03/2019

#Importing datetime module
from datetime import datetime

##Datetime for now
now = datetime.now()

#Printed datetime now in correct format
print (now.strftime('%A, %B %d %Y at %I:%M%p'))