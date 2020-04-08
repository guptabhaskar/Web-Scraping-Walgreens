from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()

driver.get("https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state=IL&city=ADDISON&from=localSearch")

delay = 10 # seconds

try:

    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

    print("Page is ready!")
except TimeoutException:

    print ("Loading took too much time!")

# res=requests.get("https://www.walgreens.com/storelocator/find.jsp?requestType=locator&state=IL&city=ADDISON&from=localSearch")

res=driver.execute_script("return document.documentElement.outerHTML")


driver.quit()
soup=bs(res,'html.parser')

for i in range(20):
	a="wag-store-locator-result-"+str(i)
	box= soup.find(id=a)

	print(box)	