import pyautogui
import time

# Game_Link:http://game2.baifumeiba.com/minigame/ydygdy/

time.sleep(0.2)
pyautogui.click(1500, 640)
pyautogui.moveTo(1500, 1090, 0.05)
pyautogui.mouseDown()
pyautogui.moveTo(1500, -1080, 0.01)
time.sleep(1)
pyautogui.mouseUp()
