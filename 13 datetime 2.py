from datetime import datetime, timedelta   

print ( 'Now'   , datetime.now() )
print ( 'Today' , datetime.today() )
print ( 'Year'  , datetime.today().year )
print ( 'Month' , datetime.today().month )
print ( 'Day'   , datetime.today().day )

# date to string
x     = datetime.today().strftime('%B, %d %Y')
print ('Date formatted ', x )
print ( type(x)  )

#string to date
x =  datetime.strptime('2019-09-25','%Y-%m-%d')
print (x , type(x))


#d =  ( input ("What is the day of your DOB? ") )
#
#m =  ( input ("What is the month of your DOB? ") )
#
#y =  ( input ("What is the year of your DOB? ") )
d = '01'
m = '01'
y ='2020'
dob = y+"/"+ m+"/"+ d

dob =  datetime.strptime(dob,'%Y/%m/%d')
print (dob)
nw = datetime.now()
delta = nw - dob  
print("interval in days", delta.days)


days = delta.days
y = days/365
r = days % 365
m = r / 30.5
d = r % 30.5
print ( "years: " ,y,"month", m, "days", d )




date1 = "2020/01/01"
date1 =  datetime.strptime(date1,'%Y/%m/%d')
print (date1)
date2 = "2020/12/31"
date2 =  datetime.strptime(date2,'%Y/%m/%d')
print (date2)
delta = date2-date1
print("interval in days", delta.days)


days = delta.days
y = days/365
r = days % 365
m = r / 30.5
d = r % 30.5
print ( "years: " ,y,"month", m, "days", d )




rage = 67  #int(input("what is your retirement age"))
rdte = dob + timedelta(days=rage*365)
print (rdte)
##
#print ( ' number of days between now and your reqtirement date', dte - datetime.now() )
#print ( ' number of days between now and retirement', (dte - datetime.now()).days, 'days' )
#
#print ( "your retirement date is: ")
#print ( "between now and your retirement date, still still have to live:" )
#print ( "Years")
#print ( "Months")
#print ( "Days")
