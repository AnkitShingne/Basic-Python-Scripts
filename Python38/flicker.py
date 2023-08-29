#! python3
# flicker.py - Searches and downloads images from flicker

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://flicker.com')

time.sleep(10)

searchElem = browser.find_element_by_name('text')
searchElem.send_keys('Stamford Bridge')
searchElem.send_keys(Keys.ENTER)

time.sleep(5)

photoElem = browser.find_element_by_class_name('overlay.no-outline')
time.sleep(5)
photoElem.click()
#time.sleep(3)
#photoElem.send_keys(Keys.CONTROL,'s')