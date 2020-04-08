#Imports
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

# Function for scraping websites of stores on a particular URL
def scrape(url):
	driver=webdriver.Chrome()
	driver.get(url)
	delay=8 # seconds
	loadMoreBtn="//*[@id='loadMoreBtn']"
	b=False

	#Waits for full site to load
	try:
		#Wait for Load More Button to load
	    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,loadMoreBtn)))
	    b=True
	except TimeoutException:
		#If no load more button on website
	    print("No Load More Button found")
	
	#Clicks on load more if it is present
	if(b):
		while(True):
			try:
				time.sleep(delay)# time in seconds
				btn = driver.find_element_by_xpath(loadMoreBtn)
				ActionChains(driver).move_to_element(btn).click(btn).perform()
				WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,loadMoreBtn)))
			except TimeoutException:
				break

	res=driver.execute_script("return document.documentElement.outerHTML")
	driver.quit()
	soup=bs(res,'html.parser')
	l=[]
	c=True
	size=0
	while(c):
		a="wag-store-locator-result-"+str(size)
		box= soup.find(id=a)
		if(box==None):
			c=False
			break
		size=size+1
		print()
		s=str(box)
		i=s.find('/locator')
		s=s[i:]
		i=s.find('"')
		s="https://www.walgreens.com"+s[:i]
		l.append(s)
	return l

# State Name
state="WY"
# City Name
city="CASPER"
# URL using state name and city name
url="https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state="+state+"&city="+city+"&from=localSearch"
#Function to scrape websites of all the stores on that link
l=scrape(url)
#List of websites of each store in list l
print(l)
