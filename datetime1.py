#Write a program that outputs today’s date and time in the format ”Monday, January
#10th 2019 at 1:15pm”.

#Colin Morrow
#25/03/2019

from datetime import datetime

now = datetime.now()

print (now.strftime('%A, %B %d %Y at %I:%M%p'))