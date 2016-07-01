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

def getMenu():
	url="http://www.clarinsusa.com/"
	browser.get(url)
	browser.wait = WebDriverWait(browser, 50)
	try:
		menu=browser.find_elements_by_css_selector('ul.level-0 > li > ul.level-1 > li.level1-category > a')
		for i in menu:
			getmenu=i.get_attribute('href')
			#print getmenu
			l = io.open('get_link_menu.csv', 'a', encoding='utf8')
			l.write(getmenu+"\n")
	except NoSuchElementException:
		menu = ""
		print "Menu cannot found!"
				
try:
	getMenu()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()