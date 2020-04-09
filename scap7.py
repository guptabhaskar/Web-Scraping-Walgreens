#Imports
from test import cities
l=cities[3500:4000]
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
def scrape(l1,url):
	count=0
	driver.get(url)
	delay=5 # seconds
	loadMoreBtn="//*[@id='loadMoreBtn']"
	b=False

	#Waits for full site to load
	try:
		#Wait for Load More Button to load
	    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,loadMoreBtn)))
	    b=True
	except TimeoutException:
		#If no load more button on website
	    #print("No Load More Button found")
	    count+=1

	
	#Clicks on load more if it is present
	if(b):
		while(True):
			try:
				time.sleep(delay)# time in seconds
				btn = driver.find_element_by_xpath(loadMoreBtn)
				# driver.execute_script("arguments[0].click();", btn)
				driver.execute_script("arguments[0].scrollIntoView(true);",btn)
				# ActionChains(driver).move_to_element(driver.sl.find_element_by_xpath(loadMoreBtn)).perform()
				ActionChains(driver).move_to_element(btn).click(btn).perform()
				WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,loadMoreBtn)))
			except TimeoutException:
				break

	res=driver.execute_script("return document.documentElement.outerHTML")
	soup=bs(res,'html.parser')
	c=True
	size=0
	while(c):
		a="wag-store-locator-result-"+str(size)
		box= soup.find(id=a)
		if(box==None):
			c=False
			break
		size=size+1
		s=str(box)
		i=s.find('/locator')
		s=s[i:]
		i=s.find('"')
		s="https://www.walgreens.com"+s[:i]
		print("\""+s+"\",",end="")
		l1.append(s)
	return l1

l1=[]
#create .csv file and write
driver=webdriver.Chrome()
for j in l:
	l1=scrape(l1,j) # list of links of all stores in jth link 
driver.quit()
print()
print()
print(l1)




