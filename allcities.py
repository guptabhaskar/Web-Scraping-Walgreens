from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

#using allstate.py
allurl=['http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=AL', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=AK', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=AZ', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=AR', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=CA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=CO', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=CT', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=DE', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=DC', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=FL', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=GA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=HI', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=ID', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=IL', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=IN', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=IA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=KS', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=KY', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=LA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=ME', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MD', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MI', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MN', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MS', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MO', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=MT', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NE', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NV', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NH', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NJ', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NM', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NY', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=NC', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=ND', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=OH', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=OK', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=OR', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=PA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=PR', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=RI', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=SC', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=SD', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=TN', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=TX', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=UT', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=VT', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=VA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=VI', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=WA', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=WV', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=WI', 'http:/www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=WY']

all_cities_links=[]
driver=webdriver.Chrome()
count1=0
for i in allurl:
	count=0
	driver.get(i)
	delay = 3 # seconds
	try:
	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

	    
	except TimeoutException:
		pass

	    

	# res=requests.get("https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state=IL&city=ADDISON&from=localSearch")

	res=driver.execute_script("return document.documentElement.outerHTML")

	soup=bs(res,'html.parser')
	box=soup.findAll(class_="row")
	for div in box:
	    links = div.findAll('a')
	    for a in links:
	    	if(len(a['href'])>3):
	    		count+=1
	    		b="http:/www.walgreens.com"+a['href']
	    		all_cities_links.append(b)
	count1+=count
	print(i[-2:]+" "+str(count))
driver.quit()
print(len(all_cities_links))
print(all_cities_links)
# AL 82
# AK 5-87
# AZ 49-136
# AR 46-182
# CA 279-461
# CO 57-518
# CT 79-597
# DE 26-623
# DC 1-624
# FL 239
# GA 146
# HI 10
# ID 21
# IL 253
# IN 99
# IA 37
# KS 36
# KY 96
# LA 67
# ME 71
# MD 86
# MA 157
# MI 131
# MN 92
# MS 56
# MO 108
# MT 9
# NE 17
# NV 12
# NH 33
# NJ 202
# NM 23
# NY 276
# NC 166
# ND 1
# OH 145
# OK 50
# OR 40
# PA 81
# PR 55
# RI 24
# SC 70
# SD 7
# TN 120
# TX 213
# UT 40
# VT 28
# VA 107
# VI 1
# WA 65
# WV 86
# WI 124
# WY 8