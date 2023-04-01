#To get current date and time we need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()
mydate = datetime.today()
# The now function returns current date and time as a datetime object

# You must convert the datetime object to a string
# before you can concatenate it to another string
# print('Today is: ' + str(mydate))

today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print(yesterday)
print(one_day)

