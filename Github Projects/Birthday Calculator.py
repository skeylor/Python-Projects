
# Birthday calculator

import datetime
x = datetime.datetime.now()

day = int(input('On what day were you born?'))
month = int(input('What month were you born?'))
current_day = x.day
current_month = x.month

if day == current_day and month == current_month:
    print('Happy Birthday')
else:
    print('It is not your birthday!!')
    