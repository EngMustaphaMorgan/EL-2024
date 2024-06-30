#!/usr/bin/python3
from pyautogui import *
location = None
extensions_shortcut = ["ctrl" , "shift", "x"]
press("win")
sleep(1)
write("cod")
sleep(1)
while location == None :
    try :
        location = locateOnScreen("03-pyautogui/pics/04-vs-code-icon.png")
        click(location.left+5,location.top+20,duration=1)
        keyDown('ctrl')
        keyDown('shift')
        press('x')
        keyUp('shift')
        keyUp('ctrl')
        sleep(1)
        hotkey('ctrl','a')
        keyDown('backspace')
        sleep(1)
        keyUp('backspace')
        write("c++ testmate")
        sleep(1)
        location = None
        while location == None :
            try :
                location = locateOnScreen("03-pyautogui/pics/05-c++-testmate.png")
                moveTo(location.left+530,location.top+55,duration=1)
                # click(location.left+800,location.top+55,duration=1)
            except :
                print("extension image not found")

    except ImageNotFoundException :
        print("icon image not found")