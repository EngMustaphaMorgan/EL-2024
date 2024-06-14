#!/usr/bin/python3

# shebang to inform linux how it will execute the current file
# beware not to write a comment before shebang as it will generate an error
# as In the incorrect usage, the presence of the comment before the shebang line
# prevents the shebang from being interpreted correctly, which can result in an error.

# single line comment

'''
Multiple line comment
'''
# Multiple line comment is not the best practice
#if you want to comment multiple line use "ctrl/"

# if you tried to execute your script now it will give permission denied error
# since the file has no execution permission for user
# to give the file user execution permission we use :
# $ chmod u+x filename.py

# first python code

# here we are using python builtin print function of python without importing
# any library that's because of the virtual machine in the interpreter of
# python that's is directly linked to library modules
print("first hello from python")
# also strings in python can be implemented using :
# - single quotation
print('Hello with single quotation')
# - double quotation
print("Hello with double quotation")
# - triple quotation but must be a function argument or assigned to a variable
# - so that python will not consider it as a comment
print('Hello with triple quotation')

# first task :
# write a python code that print your full name , birth date and email
print("Name : Mostafa Morgan ",end=",")
print ("age : 30 ", end=',')
print("email : Eng.MustaphaMorgan@gmail.com", end='\n')
#end is implemented by default as '\n'

# variables
# variables in python have an advantage named : [Dynamic Type]
# first in python there is no need to declare the type of the variable
# unlike c and cpp , alo in rust we use (let x = 5)
# in python also there is no multiple definitions so as you can see below
# x was once an int with value 5 , then it became a string with value "Mostafa"
# and finally it wa a float with value 3.5
# and that is because the presence of the garbage collector that deallocates
# the old variable from memory and then reallocates it again in a new place
# with the new type and value
# and that what defines the meaning of Dynamic type

# take in consideration also that the variable in python is not just
# a normal scalar variable like that in c and c++ , we consider it a a class
# with various methods (i.e. bitcount bitlength abs etc...)

x = 5
print(type(x))
print(id(x))

x = "Mostafa"
print(type(x))
print(id(x))

x=3.5
print(type(x))
print(id(x))

x = int(input("please enter the value : ")) #print by default return a string so we must convert it to int for future use
x += 5

#comma operator
#----------------
x,y,z = 1,2,3
x,_,z= 1,2,3 # the _ here means to ignore the 2nd variable and it's value

# sequence data types in python
#--------------------------------
# list is sequence datatype in python like the array in c and c++ , but it can hold different datatypes
ls = [1,2.5,"Morgan",[3,4.5,"Mostafa"]]
ls = list(1,2.5,"Morgan") # defining the list using the constructor
# list can be accessed by index and it is starting by 0
ls[1] = 50 #assigning value 50 to the 2nd element in the ls list
print(ls[1:3]) #print the values in the list starting from index 1 till before index 3 (50,"Morgan")
print(ls[-1]) #print the last index in the list
print(ls[2:]) #print the list starting from index 2 till the end of the list
print(ls[1:4:2]) #print the list starting from index 1 till before index 4 with step 2
# as we can see here we can change the values in the list whenever we want so we can ay that the list is mutable
# properties of the list
#---------------------------
# collection of different datatypes
# indexed
# ordered
# mutable

 # tuples in python is just like the list but it is constant , which means that you cant change the values in it (immutable)
# properties of the tuple
#---------------------------
# collection of different datatypes
# indexed
# ordered
# immutable
tup = (1,2.5,"Morgan")
# tup[1] = 50 # will give an error tup is a tuple and tuple is immutable
print(tup[1:3])
print(tup[-1])
print(tup[2:])
print(tup[1:4:2])

# dictionary in python is constructed from keys and values , it is the literal definition of json file
# dictionary is also implemented in cpp and known ad std::map and in rust is hashmap
# in std::map in cpp we must define the types that we will gonna use in map unlike dictionary in python
# take care that no duplicate member in python dictionary since the new one will override the old one and vieversa in cpp
this_dict = {
   "brand"    : "ford" ,
   "electric" : False ,
   "year"     : 1946 ,
   "colors"   : ["red","white","black"]
}

print(type(this_dict))
print(this_dict)
print(this_dict.keys)
print(this_dict.values)
print(this_dict["brand"])
print(len(this_dict))

# set in python is a sequential datatype but it is unordered , mutable and don't allow duplicate values
# it mainly depends on the concept of hash table
# in hash table , if you want to assign any value in set , it must be processed by an algorithm named hash table
# the hash table receives what will gonna be assigned in the et and let's consider it will encrypt it  so that it will
# like a unique ID , so when we search for a specific value in set it will pa through the hash function that will result in the same
# ID assigned to this value and by this ID we can get the value we need .
names = {"john smith", "Lisa", "Mike", "Jack"}

#converting a string into a list
#-------------------------------
name = "Morgan"
print(list(name))

# if statements in python
# ----------------------------------------
a = 200
b = 33

if b>a :
    print( "b is greater htan a" )
elif a==b :
    print( "b is equal to a" )
else :
    print( "a is greater than b" )

# short handed if
#--------------------
a = 200
b = 33

print(a) if a == b  else print(b)

# ternary operator
#--------------------------
print(a) if a > b else print("=") if a == b else print(b)

# task 2
#-----------------
# write a python code that handle the following login system
# userName = [Ali , Ahmed , Amr]
# passWord = [1394, 6078  , 9345]
# if the data entered is correct , the system shall show a wlcome mesage 
# if not the system will print incorrect entry

credentials = {
    "Ali"   : 1394 ,
    "Ahmed" : 6078 ,
    "Amr"   : 9345
}

def login_system(username , password) :
    if username in credentials and credentials[username] == password :
        print(f"welcome {username}!")
    else :
        print("incorrect entry")

user = input("please enter your username : ")
userpass = int(input("please enter your password : "))

login_system(user, userpass)


# loops in python
#-------------------

# while loop
#---------------
i = 0
while(i < 5):
    print(i)
    i+=1

# for loop 
#--------------
for i in range (0, 4) :
    print(i)

# break vs continue
#---------------------
for i in range(0, 10) :
    if i%2 == 0 :
        break
    print(i,"odd")

for i in range(0, 10) :
    if i%2 == 0 :
        continue
    print(i,"odd")

# else in for loop (eftkasa)
for i in range (10) :
    print(i)
else :
    print("finish")

# nested for loop
#------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj :
    for y in fruits :
        print(i,y)

# Modules in pytjon 
#----------------------
# 1- psutil
#-----------------
import psutil

# get CPU usage percentage
print("CPU Usage: ",psutil.cpu_percent())

# get memory usage statistics
#------------------------------
memory = psutil.virtual_memory()

print("Total Memory = ",memory.total/1000000000, "G")
print("Available Memory = ",memory.available/1000000000, "G")
print("Used Memory = ",memory.used/1000000000, "G")
print("Memory percentage = ",memory.percent)

# get disk usage percentage
#-----------------------------
disk = psutil.disk_usage('/')
print("Total disk space",disk.total/1000000000, "G")
print("Ued disk space",disk.used/1000000000, "G")
print("Free disk space",disk.free/1000000000, "G")
print(" Disk usage percentage",disk.percent)


# to open the GUI of the directory you want 
# nautilus [path to your directory]

# favourite folder script
#----------------------------
import os

# implement a list with the directories you want 
favouriteFolder = []

val = int( input("please select your directory (insex start with 0): ") )

os.open(r"nautilus {}".format(favouriteFolder[val]))


#print the current date and time
#---------------------------------
import datetime
datetime.datetime.now()

