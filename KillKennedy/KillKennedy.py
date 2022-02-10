import pyautogui
import time

# game_link: https://beibao233.github.io/Marksman/

png = r'C:\\Users\\elfdobby\\pythonProject\\GameGuaBi\\KillKennedy\\02.jpg'


def kill():
    time.sleep(0.01)
    left, top, width, height = pyautogui.locateOnScreen(png)
    center = pyautogui.center((left, top, width, height))
    pyautogui.click(center)
    print('Kill!')


while True:
    if pyautogui.locateOnScreen(png):
        kill()

    else:
        pyautogui.scroll(500)
        print('NEXT')
