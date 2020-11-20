import datetime

# datetime class from datetime module and using now() method
datetime_object = datetime.datetime.now()
print(datetime_object)
# date class from datetime module and using today() method
date_object = datetime.date.today()
print(date_object)
# dir() function to get a list containing all attributes of a module
print(dir(datetime))
d = datetime.date(2019, 4, 13)
print(d)
# We can import date class from the datetime module
from datetime import date

a = date(2019, 5, 13)
print(a)

today = date.today()
print("Current date =", today)

# We can get year, month, day, day of the week etc. from the date object
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# A time object instantiated from the time class represents the local time.
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

print("hour =", d.hour)
print("minute =", d.minute)
print("second =", d.second)
print("microsecond =", d.microsecond)

# datetime class that can contain information from both date and time objects.
from datetime import datetime

# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

# A timedelta object represents the difference between two dates or times.
from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2

print("t3 =", t3)

# The strftime() method returns a string representing date and time using date, time or datetime object.
# converts a datetime object containing current date and time to different string formats.
from datetime import datetime
# current date and time
now = datetime.now()

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

# The strptime() method creates a datetime object from the given string.
# You cannot create datetime object from every string. The string needs to be in a certain format.
from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

# Current date in different formats
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
