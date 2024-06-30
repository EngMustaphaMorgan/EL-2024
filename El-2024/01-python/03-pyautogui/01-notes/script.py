#!/usr/bin/python3
import pyautogui
from time import sleep
import pyfiglet

# print(pyfiglet.figlet_format("#__________________________________________________________________"))
# print(pyfiglet.figlet_format("Mouse Cmds"))
# print(pyfiglet.figlet_format("#__________________________________________________________________"))

# sleep(5)
# to detect the current co-ordinates of the mouse
# print(f"current co-ordinates of the mouse is : {pyautogui.position()}")

# To check if XY coordinates are on the screen, pass them (either as two integer arguments or a single tuple/list arguments
# with two integers) to the onScreen() function, which will return True if they are within the screen’s boundaries
# and False if not.
# pyautogui.onScreen(0,0)

# to click on a specific icon in a specfic position
# using the pyautogui.position() method we got the position of the mouse
# pointing to the specific icon we want to click (i.e. x=21 , y=748)
# pyautogui.click(21,748)

# to know the dimenions of your screen
# pyautogui.size()

# to move the mouse to a specific position
# we have two methods to move the cursor of the mouse
# when using None a an argument representing x/y coordinates
# it means the current position of the mouse 
# to a specfic position first is :
# moveto(x coordinates , y coordinates , duration)
# pyautogui.moveto(21,748)
# move() is just like moveto() but it is used when 
# If you want to move the mouse cursor over a few pixels
# relative to its current position,
# move(x coordinates , y coordinates)

# to double or triple or left click on a specific icon in apecific position
# pyautogui.doubleClick(21,748)
# pyautogui.tripleClick(21,748)
# pyautogui.leftClick(21,748)

# to scroll upwards and downwards
# pyautogui.scroll(25)  # scroll upwards
# pyautogui.scroll(-25) # scroll downwards

# to select a specific region in a window (i.e. select multiple files)
# pyautogui.mouseDown() # to select a specifc region in a window
# sleep(3)
# pyautogui.mouseUp()   # release the mouse


# print(pyfiglet.figlet_format("#__________________________________________________________________"))
# print(pyfiglet.figlet_format("Keyboard Cmds"))
# print(pyfiglet.figlet_format("#__________________________________________________________________"))

# to print keyboard keys
# print(pyautogui.KEYBOARD_KEYS)

# to execute a shortcut like ("ctrl+c" for copy)
# sleep(10)
# print("end")
# pyautogui.hotkey('ctrl','c')
# sleep(10)
# pyautogui.hotkey('ctrl','v')

# to write a text
# text = "this text is written by pyautogui"
# pyautogui.write(text)

# to press on a specific key in the keyboard
# take care it takes only one string as an argument
# so if you need to press on multiple keys
# assign those keys to a list
# key_combine = ["enter","c"," "]
# pyautogui.press(key_combine,presses=5) # presses define the number of times you want to press that key

# to long press on a specific key 
# pyautogui.keyDown("ctrl")
# pyautogui.press("a")

# to realease the key in keydown
# pyautogui.keyUp("ctrl")

# to make a countdown
# pyautogui.countdown(5)

# to create an alert 
# pyautogui.alert(text="This is a pyautogui alert",title="pyautogui alert",button="continue",timeout=5000) #timeout will make msg disapperar after given time in ms

# to create a confirmation message
# pyautogui.confirm(text="confirm on pyautogui alert", title="alert confirm", buttons=["Ok","Cancel"],timeout=5000)

# to create user password
# pyautogui.password(text="enter your pass",title="login",default="0000",mask="*") 
# sleep(20)
# print(pyautogui.position())
# to locate a picture on screen
#________________________________________________________________
# run a pyhton script using pyautogui
#________________________________________________________________
# location = None
# while location == None :
#     try : # we moved the try inide the while loop inorder to avoid exception and force the logic to wait till it find the image
#         location = pyautogui.locateOnScreen("./03-pyautogui/pics/01-run-vscode-python-script.png")
#         pyautogui.moveTo(location.left+14, location.top+16)
#         pyautogui.click()
#     except pyautogui.ImageNotFoundException :
#         print("Image not found")

#________________________________________________________________
# open terminal using pyautogui
#________________________________________________________________
# pyautogui.hotkey("ctrl","alt","t")
# location = None
# pyautogui.press("win")
# sleep(1)
# pyautogui.write("termin")

# while location == None :
#     try :
#         location = pyautogui.locateOnScreen("./03-pyautogui/pics/03-terminator-icon.png")
#         pyautogui.click(location.left,location.top,duration=1)
#     except pyautogui.ImageNotFoundException :
#         print("Image not found")

