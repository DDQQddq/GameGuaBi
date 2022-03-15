from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import cmd_form

# port = input("请输入端口号（5003/5004）: ")
# if int(port) == 5003:
#     port = "auto"
#     port_dir = "127.0.0.1" + port
# else:
#     port_dir = "127.0.0.1" + str(port)
port = 5003
con_port = "auto"
cmd_form.command(str(port), con_port)
space_dir = "https://space.bilibili.com/522426854/dynamic"
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
driver = webdriver.Chrome(options=option)
driver.get("https://space.bilibili.com/522426854/dynamic")

zan_button = driver.find_element(By.CLASS_NAME, "custom-like-icon zan")
print(zan_button)
