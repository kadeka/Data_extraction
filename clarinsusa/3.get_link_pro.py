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

def getLinkPro():
	with open('get_link_subMenu.csv', 'rb') as f:
	    for row in f:
	    	print row
	    	browser.get(row)
	    	browser.wait = WebDriverWait(browser, 30)
	    	try:

	    		popup=browser.find_element_by_css_selector("div#newsletter-overlay-container  > a > div.newsletter-overlay-close")
	    		popup.click()
	    	except NoSuchElementException:
	    		print "No popup to close"	
	    	for i in range(1,10):
	    		print "scroll"
	    		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    		time.sleep(2)
	    	try:
	    		allProductLink=browser.find_elements_by_css_selector("div.product-image > a.thumb-link")
	    		k=len(allProductLink)
	    		print k
	    		for e in allProductLink:
	    			getAllProLink=e.get_attribute("href")
	    			print getAllProLink
	    			l=io.open('get_link_pro.csv', 'a', encoding='utf8')
	    			l.write(getAllProLink+"\n")
	    	except NoSuchElementException:
	    		print "No link"
				
try:
	getLinkPro()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()