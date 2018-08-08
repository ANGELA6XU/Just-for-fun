# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# print(driver.title)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(3)
# driver.close()

# automate boring stuff with pyautogui, controlling keyboard and mouse

import pyautogui
#print(pyautogui.size())

# mouse movement, parameters are x and y - coordinates according to the computer system.
pyautogui.moveTo(800, 50)

# mouse click, parameters are x,y - coordinates, and movement duration.
pyautogui.click(800, 50, duration = 1)

