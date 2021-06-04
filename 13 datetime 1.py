"""
Number of ticks since 12:00am, January 1, 1970: 1591290336.8860185
-----gm time----------- time.struct_time(tm_year=2020, tm_mon=6, tm_mday=4, tm_hour=17, tm_min=5, tm_sec=36, tm_wday=3, tm_yday=156, tm_isdst=0)
"""
import time

mytime = time.time()
print ( "Number of ticks since 12:00am, January 1, 1970:", mytime)


print ( "-----gm time-----------",  time.gmtime())

print("\nyear:"   , ( time.gmtime().tm_year) )
print("tm_hour:"  , time.gmtime().tm_hour)
print( 'tm_isdst' , time.gmtime().tm_mday)
print( 'tm_isdst' , time.gmtime().tm_isdst)
# 
localtime = time.localtime( )
print ("localtime = time.localtime( )")
print ( localtime )
##time.localtime([secs]), Like gmtime() but converts to local time.
#
#
print ("1 ----------------")
print ( time.asctime(time.localtime())  )  # asctime formats the time in the brackets
#
result = time.localtime()
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)






