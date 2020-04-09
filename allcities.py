import allstate

from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


allurl=allstate.get_statelinks()
all_cities_links=[]
size=0
for i in allurl:
	driver=webdriver.Chrome()

	driver.get(i)

	delay = 3 # seconds

	try:

	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

	    
	except TimeoutException:
		pass

	    

	# res=requests.get("https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state=IL&city=ADDISON&from=localSearch")

	res=driver.execute_script("return document.documentElement.outerHTML")


	driver.quit()
	soup=bs(res,'html.parser')
	box=soup.findAll(class_="row")
	all_cities_links.append([])
	for div in box:
	    links = div.findAll('a')
	    for a in links:
	    	if(len(a['href'])>3):
	    		b="http:/www.walgreens.com"+a['href']
	    		all_cities_links[size].append(b)
	size=size+1

print(all_cities_links)