#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#
#
#
#------------------------------------------------------------------------------------------------------------------

# import favouriteLinks module 
from favouriteLinks import favouriteLinks as open_url


# prompt the user to input the desired link to launch
# 01-yocto
# 02-openembedded
# 03-cppreference

url = input("please choose the site you want to launch \n 01-Yocto \n 02-openembedded \n 03-cppreference \n")
url:str = url.casefold()

#oprn the given url
open_url(url)

