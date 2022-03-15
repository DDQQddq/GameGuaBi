import pyautogui as ag
import Selenium.cmd_form
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

port = 5003
con_port = "auto"
Selenium.cmd_form.command(str(port), con_port)
time.sleep(0.2)
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
ag.moveTo(800, 500)
browser.get("http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp")
bb = browser.find_element(By.XPATH, "/html/body/div[2]/div[5]/ul/li[1]/a/i")
ActionChains(browser).move_to_element(bb).click(bb).perform()
time.sleep(0.1)

ag.scroll(-1000)
ag.click(940, 940)
time.sleep(0.3)
ag.click(610, 860)
time.sleep(0.2)
ag.click(1130, 940)
time.sleep(5)
ag.click(1890, 20)
ag.moveTo(1000, 540)
