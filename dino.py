import pyautogui
import time

time.sleep(3)
color = [172,172,172]
while True:
    mousepos = pyautogui.position()
    if(list(pyautogui.pixel(mousepos[0], mousepos[1])) == color):
        print("jump")
        pyautogui.press("up")
    #time.sleep(0.025)
