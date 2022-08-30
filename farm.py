from turtle import left, right
import pyautogui as py
import time
import keyboard

def inicio():
    py.press("e")
    time.sleep(1)
    py.keyDown("left")
    time.sleep(1.1)
    py.keyUp("left")
    time.sleep(0.5)
    py.keyDown("down")
    time.sleep(0.1)
    py.keyUp("down")
    time.sleep(0.5)

def takeelevators():
    py.press("f")
    time.sleep(0.5)
    py.click(909,623)
    time.sleep(0.5)
    py.click(909,623)
    time.sleep(0.5)
    py.click(1566,176)

def breakelevators():
    time.sleep(0.5)
    py.keyDown("left")
    time.sleep(0.1)
    py.keyUp("left")
    time.sleep(0.5)
    py.press("1")
    time.sleep(0.5)
    x=1
    while x<=200:
        py.click()
        time.sleep(0.2)
        x+=1
        if keyboard.is_pressed("f10"):
            break;

def putresource():
    time.sleep(0.5)
    py.keyDown("right")
    time.sleep(0.1)
    py.keyUp("right")
    time.sleep(0.5)
    #### dedi 1 ####
    py.keyDown("up")
    time.sleep(0.1)
    py.keyUp("up")
    time.sleep(0.5)
    py.press("e")
    time.sleep(1)
    #### dedi 2 ###
    py.keyDown("up")
    time.sleep(0.1)
    py.keyUp("up")
    time.sleep(0.5)
    py.press("e")
    time.sleep(1)
    #### dedi 3 ####
    py.keyDown("right")
    time.sleep(0.3)
    py.keyUp("right")
    time.sleep(0.5)
    py.press("e")
    time.sleep(1)
    ### dedi 4 ####
    py.keyDown("down")
    time.sleep(0.1)
    py.keyUp("down")
    time.sleep(0.5)
    py.press("e")
    time.sleep(1)
    ### dedi 5 ###
    py.keyDown("down")
    time.sleep(0.1)
    py.keyUp("down")
    time.sleep(0.1)
    py.keyDown("left")
    time.sleep(0.3)
    py.keyUp("left")
    time.sleep(0.5)
    py.press("e")
    time.sleep(1)

while True:
    if keyboard.is_pressed("f1"):
        inicio()
        x=0
        while x<=20:
            takeelevators()
            breakelevators()
            putresource()
            if keyboard.is_pressed("f10"):
                break;
            x+=1
        if keyboard.is_pressed("f10"):
            break;
