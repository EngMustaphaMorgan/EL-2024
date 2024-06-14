#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#               import os module
#               get environ from os
#               print each enviroment variable
#------------------------------------------------------------------------------------------------------------------

#import os module
import os

# get all enviroment variables
env_vars = os.environ 

#print each enviroment variable
for key, value in env_vars.items() :
    print( f" {key} : {value} " )