from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


option = webdriver.ChromeOptions()
# option.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
# option.add_argument('headless')  设置option
browser = webdriver.Chrome(options=option)
browser.get("http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp")
user_name_input = browser.find_element(By.ID, "username")
# 括号内的引号内为你本人的学号
user_name_input.send_keys('xxxxxxxx')
user_pwd_input = browser.find_element(By.ID, "password")
# 括号内的引号内为你本人翱翔门户的密码
user_pwd_input.send_keys('xxxxxxxx')
login_button = browser.find_element(
    By.XPATH, "/html/body/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/div[1]/form/div[4]/div/input[5]")
ActionChains(browser).move_to_element(login_button).click(login_button).perform()
print('点击登陆')
time.sleep(0.1)
# aa = browser.find_element(By.XPATH, "/html/body/div/div[5]/ul/li[1]/a/i")
# ActionChains(browser).move_to_element(aa).click(aa).perform()
# print('点击登陆')
# time.sleep(0.1)
browser.get("http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp")
bb = browser.find_element(By.XPATH, "/html/body/div[2]/div[5]/ul/li[1]/a/i")
ActionChains(browser).move_to_element(bb).click(bb).perform()
time.sleep(0.1)
cc = browser.find_element(By.XPATH, "/html/body/div[3]/form/div[5]/div[16]/div")
ActionChains(browser).move_to_element(cc).click(cc).perform()
time.sleep(0.1)
dd = browser.find_element(By.XPATH, "/html/body/div[3]/form/div[6]/div[2]/div[11]/label/div[1]/i")
ActionChains(browser).move_to_element(dd).click(dd).perform()
time.sleep(0.1)
time.sleep(4)
browser.quit()
