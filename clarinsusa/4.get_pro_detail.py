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
	with open('get_link_pro.csv', 'rb') as f:
	    for row in f:
	    	print row
	    	browser.get(row)
	    	browser.wait = WebDriverWait(browser, 30)
	    	try:
	    		title=browser.find_element_by_css_selector("div.pdp-right-top > div > h1").get_attribute('textContent')
	    	except:
	    		title=' '
	    		print "No title"
	    	try:
	    		price=browser.find_element_by_css_selector("div.product-price > span.price-sales").get_attribute('textContent')
	    	except:
	    		price=' '
	    		print "No price"
	    	try:
	    		size=browser.find_element_by_css_selector("div.pdp-single-size-value").get_attribute('textContent')
	    	except:
	    		size=' '
	    		print "No size"
	    	try:
	    		skintype=browser.find_element_by_css_selector("div.product-skin-type > ul > li:nth-child(1) > span.value").get_attribute('textContent')
	    	except:
	    		skintype=' '
	    		print "No skintype"
	    	try:
	    		texture=browser.find_element_by_css_selector("div.product-skin-type > ul > li:nth-child(2) > span.value").get_attribute('textContent')
	    	except:
	    		texture=' '
	    		print "No texture"
	    	try:
	    		value=[]
	    		imgurl=browser.find_elements_by_css_selector("#product-content > div.product-thumbnails.pdp-prdimage-thumbnails img")
	    		for i in imgurl:
	    			getImage=i.get_attribute("src")
	    			print getImage
	    			value.append(getImage)
	    	except:
	    		imgurl=' '
	    		print "No imgurl"
	    	obj={
	    		"Title":title,
	    		"Price":price,
	    		"Size":size,
	    		"Skintype":skintype,
	    		"Texture":texture,
	    		"Image":value
	    	}
	    	myStr=json.dumps(obj)
	    	fs=open("get_pro_detail.json",'a')
	    	fs.write(myStr+",\n")			
try:
	getLinkPro()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()