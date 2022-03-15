from selenium import webdriver
import cmd_form
from selenium.webdriver.chrome.options import Options

port = 5003
con_port = "auto"
cmd_form.command(str(port), con_port)
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
driver = webdriver.Chrome(options=options)
driver.get('https://www.csdn.net/')
driver.maximize_window()

js = "window.open('https://blog.csdn.net/DQElfDobby20')"
driver.execute_script(js)
window = driver.window_handles
driver.switch_to.window(window[-1])
