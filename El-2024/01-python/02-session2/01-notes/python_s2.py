#!/usr/bin/python3

#using pyfiglet
# import pyfiglet
# print(pyfiglet.figlet_format("EL2024-Python-Session2"))


# shorthanded for
#-----------------
# def fun1() :
    # [print(i) for i in range (10) if i%2 == 0]


# def fun2() :
    # shorthanded for is similar to the following logic
    # for i in range(10) :
    #     if i%2 == 0 :
    #         print(i)

# shorthanded have a smaller footprint and execution time than original for loop in python
# by diving into the disassembly of both logic we will prove that 
# import dis
# print( "disassembly of fun1 using shorhanded for" )
# x = dis.Bytecode(fun1).dis()
# print(x)
# print( "disassembly of fun2 using original for" )
# y = dis.Bytecode(fun2).dis()
# print(y)

# in this session and the previous one we discussed some modules
# and saw how much module can  help u develop  many smart applications 
# example os , pyfiglet , dis , calendar , datetime , requests , etc
# but if it is your first time to deal with a specific module
# for example requests to go to a specific website (i.e. athan)
# when you run your code utilising this module it will through an error
# since this module is not installed "Module not found"
# so we need the package resource in order to install that module 
# pyhton has a specific tool called pip which is a package manager 
# by which you can (install/remove/list) packages oe install another tool by
# which you can search for a specific package
# you can see methods provided by pip using 
# pip --help  
# from this methods we can find freeze method which list all the packages installed by pip
# also you can find search method (it doent work on some machines)
# that's why we install pip_search tool to search for a specific package
# but take care that there are various versions for pip
# pip --version
# for example here we will find that the pip installed on this machine 
# is for installing packages for python3
# let's talk with pyhton
# we will use gTTs package to convert text into speech
# from gtts import gTTS
# import vlc

# myobj = gTTS(
#     text = 'صَبَح تا تا 2 في 3', lang = 'ar' , slow = False
# )

# saving the conveerted audio in a mp3 file 
# myobj.save("welcome.mp4")

# playing the converted file
# p = vlc.MediaPlayer("./welcome.mp4")
# p.play()

# while True :
#     


# pyhton as all programming languages have built-in functions
# for example (len , max etc...)
name = "Morgan"
# get the length of the given string
print(len(name))

ls = [1,8,3,4,5]
# get the max number in a list
print(max(ls))

# also pytohn have object function 
# which will be discussed later wiht the classes topic
# but in general as we said before every variable in python is an object
# from a class (i.e a package of a group of memebers and methods)
# you can access the methods of this object using dot operator (obj.)
name = "morgan"
print(name.capitalize()) # will make the first letter in the tring an uppercase
print(type(name))

# string methods
#---------------------
name = "morgan"
print(name.capitalize()) # will make the first letter in the tring an uppercase

print(name.center(12,"*")) # center the string between the fill character "*" with the supported index strlen+count-of-fill-character

print(name.casefold())
print(name.lower())

# In this example, we have two strings (string1 and string2) that are the same except for the use of the German letter “ß” in string1. 
# We use the casefold() method to convert both strings to lowercase and handle the “ß” character correctly, resulting in a case-insensitive 
# comparison that gives us the expected output.
string1 = "Straße"
string2 = "strasse"

if string1.casefold() == string2.casefold():
    print("The strings are equal (case-insensitive)")
else:
    print("The strings are not equal")

# encoding and decoding the string
# mainly used in socket programming as the socket can only handle utf-8
# there are variuos systems of encoding (i.e. ASCII , utf-8)
# for example in rust strings by default are encoded in utf-8
# utf-8 is up to 32 bit(4 bytes) and there is up to 64 bits
# utf-8 can handle arabic characters , emojies etc... 
name = "MORGAN" "ASCI encoding"
encoded_str = name.encode('utf-8')
print(encoded_str)
print(type(encoded_str))
decoded_str = name.decode('utf-8')
print(decoded_str)
print(type(decoded_str))

name = "Mostafa Morgan"
print(name.endswith("Morgan"))
print(name.startswith("Mostafa"))

name = "Mostafa Morgan"
print(name.find("Morgan"))
print(name.find("M",2)) # finds the index of "M" after index number 2

name = " Morgan "
print(name.strip()) # remove spaces before and after the string only

name = "Mostafa Morgan"
# convert string to list
print(name.split(" ")) 

name = "Mostafa"
age = 30

#printing format
#---------------------
print("name is {} and age is {} ".format(name,age))
print(f"name is {name} and age is {age} ")
print("name is %s and age is %d"%(name,age))

# converting a list to string using join
names = ["How", "are", "you", "doing", "today"]
print(" ".join(names))

# raw string is also in cpp
raw = r"hi \n hello"
print(raw)

# to find a specific method in python 
# got to python shell ($ python3)
# get all the supported methods for a specific class ($ dir(str))
# help(method-name) ($ help(str.split))

# functions in python 
    # Normal (void - return)
    # value (assign , default) {for the arguments of the function}
    # variadic argument ( (*) tuple - (**) dict )   

# example on variadic function (tuple)
def my_fun(*kids) :
    print(f"the youngest child is {kids[2]}")
    print(type(kids))

my_fun("Morgan" , "Mostafa", "Bilal")

# example on variadic function (tuple)
def my_fun(**arg) :
    print(arg["name"])
    print(arg["age"])
    print(arg["email"])

my_fun( name="Mostafa", age=30, email="eng.mustaphaIbrahim@gmail.com" )

# global variables in python
x = 555
def fun() :
    x = 222
    print(f"local to fun var x is {x}")
    print(f"address of local to fun var x is {id(x)}")

fun()
print(f"global var x is {x}") # a different variable from the local to function variable
print(f"address of global var x is {id(x)}")

# using global in function fun inform the function that it will
# execute the variable inide it i a global one  
x = 555
def fun() :
    global x 
    x = 222
    print(f"local to fun var x is {x}")
    print(f"address of local to fun var x is {id(x)}")

fun()
print(f"global var x is {x}") 
print(f"address of global var x is {id(x)}")

# lambda expression in python
# lambds expresion is widely used in all programming languages except c
# but in pyhton it has limited features
# lambda expression is an anonyomous function which means function with no name 
# and can be implemented anywhere in your code (i.e. inide a function / assigned to a variable etc...)
# syntax (function-name = lambda input-argumnet1 , input-argument2 .... implemented logic)
# but lambda expression in python must be implemented in a single line
# the most common use of lambda expression is in call back functions in most of languages anf capturing feature in cpp
# in other words from c point of view we can ay that lambda expression return a pointer to function that can be asigned to a variable 
# so that you can use this variable as the function
# check filter , reduce and map methods
x = lambda a,b : a+b 
print(x(5,6))

ls = [1,2,3,4,5,6,7,8,9,10]

# this line implements the lambda expression on each element of the given list
# the output will be in the form of a list and will be printed using print()
print(list( filter( lambda x : x%2==0, ls)  ))

# Modules 
#----------------
#write a code to find automatically bitcoin rate

# import requests module to end requests to a specific website (URL)
import requests
from pprint import pprint

# gets the info from the given website in the form of json file
url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# print the jon file in well formatted 
pprint(url.json())

# to know the path of a specific module using importlib module
import importlib

# printting the path of requests modules using import_module method from importlib module
print(importlib.import_module("requests"))

# list methods 
ls = [1,2,3,4,5,"Moatasem","costa","Morgan"]

# append a new element in list  
ls.append("junction")

# copy in lists
ls2 = ls
ls2.append(4)

# when printing ls and ls2 we will find that the append of 4 is executed on both lists
# since the copy made here is a shallow copy which means that both ls and ls2 access the same data in the same location
# so if we want to implement deep copy which means that ls2 will have a copy of ls in another location we can use .copy() method
print(ls2)
print(ls)

# extend a list , adding more than one element to the list (i.e. adding a list to another list) 
ls.extend(ls2)
ls.extend([4.8,5.6])

# isnert an element in a specific index in list
ls.insert(3,"30") # inserts "30" in index number 3 in ls list

# to count the number of occurence of an e;ement in the lsit
ls.count(3)

# to reverse the list
ls.reverse()

#to pop the last element in the list
ls.pop()

# to get the index of any element in list
ls.index("Morgan")

# to delete any variable using delete built in keyword in python
del(ls)

ls = [100,50,65,82,23]

# for sorting the array ascendingly
ls.sort()
print(ls)

# for sorting the array descendingly
ls.sort(reverse=True)
print(ls)


