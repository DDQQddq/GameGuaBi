import os
import sys
import pyautogui
import time

png = r'C:\Users\elfdobby\pythonProject\script\ThumbsUp\05.png'

pyautogui.click(405, 1055)
pyautogui.moveTo(1100, 500)


def kill():
    time.sleep(0.01)
    left, top, width, height = pyautogui.locateOnScreen(png)
    center = pyautogui.center((left, top, width, height))
    pyautogui.click(center)
    pyautogui.moveTo(1100, 500)
    print('Bingo!')


error = 0
while error <= 5:
    if pyautogui.locateOnScreen(png):
        kill()
        error = 0

    else:
        pyautogui.scroll(-300)
        print("NEXT")
        error += 1

if error > 5:
    os.system("start.wav")
    sys.exit()
