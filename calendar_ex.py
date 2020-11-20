import calendar
# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
sample_str = c.formatmonth(2025, 1)
print(sample_str)
# Create a html calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
sample_str1 = hc.formatmonth(2025, 1)
print(sample_str1)


# Built in Exceptions
print(dir(locals()['__builtins__']))

# Example for Exception handling using try method
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)