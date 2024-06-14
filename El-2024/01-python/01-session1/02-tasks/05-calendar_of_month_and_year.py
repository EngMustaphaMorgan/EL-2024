#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#               import calendar module  
#               prompt the user to enter the year and month
#               print the calendar of a specified year and month
#------------------------------------------------------------------------------------------------------------------

#import the calendar module
import calendar

#prompt the user to input the year and month
year = int( input( " please enter the required year :  " ) )
month = int( input( " please enter the required month :  " ) )

#print the calendar of a specified year and month
print( calendar.month(year,month) )
