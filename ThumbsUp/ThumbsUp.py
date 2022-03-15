import pyautogui
import time

png = r'C:\Users\elfdobby\pythonProject\script\ThumbsUp\04.png'

pyautogui.click(405, 1055)
pyautogui.moveTo(1100, 500)


def kill():
    time.sleep(0.01)
    left, top, width, height = pyautogui.locateOnScreen(png)
    center = pyautogui.center((left, top, width, height))
    pyautogui.click(center)
    pyautogui.moveTo(1100, 500)
    print('Bingo!')


while True:
    if pyautogui.locateOnScreen(png):
        kill()

    else:
        pyautogui.scroll(-300)
        print("NEXT")
