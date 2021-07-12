# To convert a string to datetime 
from datetime import datetime
x = datetime.strptime('Jul 9 2021 8:15PM', '%b %d %Y %I:%M%p')
print(x)
# To subtract five days (last working day) from current date
from datetime import date, timedelta
y = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',y)
# To convert the date to datetime using a function 
from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
#To print next 7 days (week) starting from today
import datetime
base = datetime.datetime.today()
for x in range(0, 7):
      print(base + datetime.timedelta(days=x))