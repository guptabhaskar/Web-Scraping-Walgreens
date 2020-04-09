from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import pandas


urls=['https://www.walgreens.com/locator/walgreens-514+kirkland+street-abbeville-al-36310/id=17041', 'https://www.walgreens.com/locator/walgreens-130+south+eufaula+avenue-eufaula-al-36027/id=19668','https://www.walgreens.com/locator/walgreens-1766+coffeen+ave-sheridan-wy-82801/id=9547', 'https://www.walgreens.com/locator/walgreens-3574+montgomery+hwy-dothan-al-36303/id=13111', 'https://www.walgreens.com/locator/walgreens-2041+e+main+st-dothan-al-36301/id=7404']


finalarray=[]
for url in urls:

	driver=webdriver.Chrome()

	driver.get(url)

	delay = 3 # seconds

	try:

	    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

	except TimeoutException:
		pass


	res=driver.execute_script("return document.documentElement.outerHTML")

	driver.quit()

	soup=bs(res,'html.parser')

	box=soup.find(id="storeAddress")

	name=box.find('p').text
	address=box.find('h1').text
	moreaddress=box.find(class_="font__twenty-five").text
	phone=box.find('a')['href']
	# print()
	# print()
	# print("Data of ",end="")
	# print(name)
	# print(address)
	# print(moreaddress)
	# print(phone)
	finalday=[]
	finaltime=[]
	box2=soup.find(id="storeServiceDiv")
	if(box2==None):
		finalday.append("Temporarily Closed")
		finaltime.append("Will reopen asap")
	else:
		wait=box2.find(class_="wag-row service-row")
		morewait=wait.find(id="storeHoursList")
		day=morewait.findAll(class_="day")
		time=morewait.findAll(class_="time")
		allday=[]
		alltime=[]
		for i in range(len(day)):
			allday.append(day[i].text)
			alltime.append(time[i].text)
			
		
		finalday.append(allday)
		finaltime.append(alltime)

	
	finalarray.append({'Name':name,'Address':address,'City':moreaddress[1:moreaddress.find(',')]    ,'State':moreaddress[moreaddress.find(',')+2:moreaddress.find(',')+5]    ,'Zipcode':moreaddress[moreaddress.find(',')+5:]      ,'Phone':phone[4:],'Open-Hour':finalday+finaltime})


df=pandas.DataFrame(finalarray)

df.to_excel("A:\\temp2.xlsx")
