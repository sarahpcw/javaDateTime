from datetime import datetime
print ( datetime.today())
x =  datetime.today().strftime('%A, %dth %B %Y  ')
print (x )

print ( datetime.now())
print ( datetime.today())
print ( type ( datetime.today().year) ) #returns and integer
print ( datetime.today().month) 
print ( datetime.today().day)

print ( datetime.today().strftime('%Y-%m-%d')) # converts from date to string

dte =  datetime.strptime('2019-09-25','%Y-%m-%d') # converts from string  to date
print ( dte, type ( dte ))

"""
%a  Locale’s abbreviated weekday name.
%A  Locale’s full weekday name.
%b  Locale’s abbreviated month name.
%B  Locale’s full month name.
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	
%c Locale’s appropriate date and time representation.
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%I Hour (12-hour clock) as a decimal number [01,12].
%j  Day of the year as a decimal number [001,366].
%m  Month as a decimal number [01,12].
%M  Minute as a decimal number [00,59].
%p   Locale’s equivalent of either AM or PM.
(1) %S  Second as a decimal number [00,61].
(2)  %U  Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w  Weekday as a decimal number [0(Sunday),6].
%W  Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x Locale’s appropriate date representation.
%X Locale’s appropriate time representation.
%y Year without century as a decimal number [00,99].
%Y  Year with century as a decimal number.
%z  Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
%Z  Time zone name (no characters if no time zone exists).

"""