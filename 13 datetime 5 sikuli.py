'''
s    m     t     w     t    f    s 
0    1     2     3     4    5    6       # 4-3=1 ; 5-3 = 2; 6-3=3 
                 5Aug  6Aug 7Aug 8Aug
9Aug 10Aug 11Aug 12Aug                  
     # 0 + 3 + 1 = 4,  the day I am on + 4 representing wed,thu,fri,sat
     # 1 + 3 + 1 = 5, 
     # 2 + 3 + 1 = 6
'''

from datetime import datetime, timedelta

mydate = '2020-08-12'

mydate = datetime.strptime(mydate,'%Y-%m-%d') # convert string to date
x      = mydate.strftime('%w')
x      = int(x)
print ('Weekday Number:',  x, datetime.strftime(mydate,'%A'))

if  x == 3:              # ALSO A WEDNESDAY : subtract 7 : 12th 
    y = -7
elif x == 4 or x == 5 or x == 6 :     # AFTER A WEDNESDAY: 4 = thurs, 6Aug; 5 = fri, 7Aug;  6 = Sat,8Aug 
    y = x - 3            # 4 - 3 = 1 , so subtract 1 day from the date, 4(thursday) - 3 (wednesday)
    y = -y
elif x in ( 0,1,2 ):     # BEFORE A WEDNESDAY: 0 = sunday,9aug, 1 = mon,10Aug; 2 = tue11Aug
    y = x + 3 + 1        # add 4 (Wed value + 1) e.g. 0 + 4 = -4, so subtract 4 days from the date
    y = -y

recentwed = mydate + timedelta(days = y)
print ('Most Recent Wednesday: ' , recentwed.strftime( '%b-%d-%Y' ), recentwed.strftime( '%m/%d/%y' ))
finaldate = recentwed.strftime( '%m/%d/%y' )


