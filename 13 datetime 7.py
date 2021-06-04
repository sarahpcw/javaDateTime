from datetime import datetime, timedelta

#calculate a date in the future ( + ) e.g. retirement date
mydate = '2000-01-01'
dob= datetime.strptime(mydate,'%Y-%m-%d') # convert string to date
print ( dob)
print ('retirement date is : ' , dob + timedelta(days = 65*364.25))

#calculate a date in the past ( - ) e.g. age
x =  (datetime.now() - dob ) 
print ('current age is: ', x)
print ('current age is: ', int( x.days/364.25) , 'years')
print ('current age in days:', x.days)

##subtract dates from another, returning number of days
cmas = datetime.strptime('2020-12-25','%Y-%m-%d')
print ( ' number of days between now and Christmas', cmas - datetime.now() )
print ( ' number of days between now and Christmas', (cmas - datetime.now()).days, 'days' )


# what is your dob
# what is your retirement age
# calc the retirement date
# how many years until retirement
# how many months until retirement
# how many days until retirement

movies = ['rambo','bambi', 'rambo','bambi', 'rambo','bambi', 'schrek']
days = ['m','t','w','th','f','s','su']