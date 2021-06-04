from datetime import datetime, timedelta  

print ( datetime.today() + timedelta(days=2)  )  # adds 2 days
print ( datetime.today() + timedelta(days=-2)  )  # subtracts 2 days

mydate =  datetime.today() + timedelta(days=-2)
print ( mydate.strftime('%m/%d/%Y'))

print ( 'Today', datetime.today().strftime('%w'))
#
mydate = '2000-01-01'
dob= datetime.strptime(mydate,'%Y-%m-%d')
print ( dob)
print ('retirement date is : ' , dob + timedelta(days = 65*364.25))


print ( datetime.now() + timedelta(days=1)  ) #Add 1 day  
print ( datetime.now() - timedelta(seconds=60)  ) #Subtract 60 seconds 
print ( datetime.now() + timedelta(days=1,minutes=60)  ) #Pass multiple parameters (1 day and 5 minutes)  

#
mydate = '2000-01-01'
dob= datetime.strptime(mydate,'%Y-%m-%d')
print ( dob)
dte = datetime.today()
x =  dte - dob
print ( x.days)

