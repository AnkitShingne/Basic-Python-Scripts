#!python3
# gmail.py - Logs into email account and sends an email.

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys(sys.argv[1])
emailElem.send_keys(Keys.ENTER)

time.sleep(2)

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(sys.argv[2])
passwordElem.send_keys(Keys.ENTER)

time.sleep(10)

compose = browser.find_element_by_class_name('T-I.J-J5-Ji.T-I-KE.L3')
compose.send_keys(Keys.ENTER)

time.sleep(10)

sendElem = browser.find_element_by_class_name('vO')
sendElem.send_keys(sys.argv[3])

time.sleep(5)

textElem = browser.find_element_by_class_name('Am.Al.editable.LW-avf.tS-tW')
textElem.send_keys(sys.argv[4:])

time.sleep(5)

sendButton = browser.find_element_by_class_name('T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
sendButton.send_keys(Keys.ENTER)

time.sleep(5)

symbol = browser.find_element_by_class_name('gb_D.gb_Ra.gb_i')
symbol.send_keys(Keys.ENTER)

time.sleep(5)

signout = browser.find_element_by_class_name('gb_Jb.gb_fg.gb_ng.gb_Xe.gb_3c')
signout.send_keys(Keys.ENTER)