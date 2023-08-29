#! python3
# 2048.py - Plays the game automatically

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://2048game.com')

time.sleep(5)

htmlElem = browser.find_element_by_xpath("//div[@class = 'game-container']")
htmlElem.click()
time.sleep(5)
while True:
	htmlElem.send_keys(Keys.UP)
	time.sleep(1)
	htmlElem.send_keys(Keys.RIGHT)
	time.sleep(1)
	htmlElem.send_keys(Keys.DOWN)
	time.sleep(1)
	htmlElem.send_keys(Keys.LEFT)
	time.sleep(1)
	