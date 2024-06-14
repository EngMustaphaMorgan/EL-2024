#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#              this code asks the user to enter a letter 
#              it checks if the letter is vowel or not
#              prints the letter is vowel or un-vowel
#               
#------------------------------------------------------------------------------------------------------------------

# check if the input letter is vowel or not 
def isvowel( x ) :
    if ( x == "a" or x == "A" or
         x == "e" or x == "E" or
         x == "i" or x == "I" or 
         x == "o" or x == "O" or
         x == "u" or x == "U" ) :
        print("vowel")
    else :
        print("un-vowel")

input_letter = ""

while(input_letter != "*"):
    # enter the letter
    input_letter = input("please enter a letter :  ")

    #check if the input letter i the terminator or not 
    if input_letter == "*" :
        break
    
    # check if the given letter is vowel or not
    isvowel(input_letter)


