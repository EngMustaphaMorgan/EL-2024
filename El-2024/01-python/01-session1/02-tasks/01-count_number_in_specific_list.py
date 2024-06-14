#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#               this code asks user to create a lsit with the deired input and size
#               it checks on the type of the user input and convert it to it's proper type
#               it aks the user about the specific number needed to find it's occurrence_count
#               it prints the occurrence_count
#------------------------------------------------------------------------------------------------------------------


# initialize an empty list to store user inputs
user_list = []

# ask the user how many elements they want to input
num_elements = int(input( "how many elements do ypu want to add in the list ?  " ))


# use a loop to get the element form the user
for list_size in range(num_elements) :

    element = input(f"Enter element {list_size}: ")

    # Try converting to int
    try:
        user_list.append(int(element))
        print(f"Input is an integer: {element}")
    except ValueError:
        # If conversion to int fails, try float
        try:
            user_list.append(float(element))
            print(f"Input is a float: {element}")
        except ValueError:
            # If conversion to float also fails, it's a string
            user_list.append((element))
            print(f"Input is a string: {element}")

# define the number needed to find it's occurence count
numbertocheck = int(input(("please enter the number needed to find it's occurence count :  ")))

# get the number of occurence of the given number in the list
occurrence_count = user_list.count(numbertocheck)

#print the given number occured n times in the list
print(f"the given number {numbertocheck} is found in the given list {occurrence_count} times")