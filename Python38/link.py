#! python 3
# link.py - To download links and ignore if not found.

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://goal.com')
time.sleep(15)
links = browser.find_elements_by_partial_link_text('haaland')
print(links)
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	type(res)
	if res.status_code == 404:
		print('Broken Link')

