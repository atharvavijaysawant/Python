
'''
import calendar
print(calendar.calendar(1990))

import calendar
m=calendar.month(2001,6)
print(m)

print(calendar.calendar(2006))
'''
import datetime
date=datetime.datetime.now()
print(date)
print(date.strftime("%d-%m-%y"))
print(date.strftime("%A"))
print(date.strftime("%b"))
print(date.strftime("%y"))
      
