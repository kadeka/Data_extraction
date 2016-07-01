import time
import io
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import selenium 
import re
from selenium.webdriver.support.ui import Select
import urllib
import json
import csv
import traceback
reload(sys)
sys.setdefaultencoding("UTF8")
pros = ""
cons=""
best_uses=""
browser = webdriver.Firefox()

def getSubMenu():
	url="http://www.clarinsusa.com/"
	browser.get(url)
	browser.wait = WebDriverWait(browser, 50)
	try:
		sub=browser.find_elements_by_css_selector('ul.level-3 > li > a')
		for i in sub:
			getsub=i.get_attribute('href')
			print getsub
			l = io.open('get_link_subMenu.csv', 'a', encoding='utf8')
			l.write(getsub+"\n")
	except NoSuchElementException:
		sub = ""
		print "subMenu cannot found!"
				
try:
	getSubMenu()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()