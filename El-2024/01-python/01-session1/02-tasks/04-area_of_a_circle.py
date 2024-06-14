#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#               this code caluclates the area of a circle 
#               given the raduis of a circle
#               area = pi*(r**2)
#------------------------------------------------------------------------------------------------------------------

# value of pi is a constant value please dont change it 
const_pi = 3.14

# insert the radius of the circle
raduis = int( input(" please enter the raduis of the circle :  ") )

# area_of_circle = pi * (raduis**2)
area_of_circle = const_pi * (raduis**2) 

#print area of circle with the given raduis
print(f"area of circle with raduis {raduis} is {area_of_circle}")