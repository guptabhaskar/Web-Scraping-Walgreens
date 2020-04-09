from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


def get_statelinks():
	driver=webdriver.Chrome()

	driver.get("https://www.walgreens.com/storelistings/storesbystate.jsp?requestType=locator")

	delay = 3 # seconds

	try:

	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

	    
	except TimeoutException:

	    pass

	# res=requests.get("https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state=IL&city=ADDISON&from=localSearch")

	res=driver.execute_script("return document.documentElement.outerHTML")


	driver.quit()
	soup=bs(res,'html.parser')
	all_state_links=[]
	box=soup.findAll(class_="col-xl-3 col-lg-3 col-md-3")
	for div in box:
	    links = div.findAll('a')
	    for a in links:
	    	b="http:/www.walgreens.com"+a['href']
	    	all_state_links.append(b)

	        # print("http:/www.walgreens.com/" + a['href'])
	return all_state_links
get_statelinks()
