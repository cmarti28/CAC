from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import urllib3
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional

#Set to HEADLESS Chrome Driver (UNCOMMENT BELOW LINE)
#driver = webdriver.Chrome(chrome_options=options) #un-comment for headless
#driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4')

#Set to Chrome Driver (UNCOMMENT BELOW LINE TO SEE BROWSER SIMULATED ACTIONS)
print('\n---NOW STARTING CHROME SERVER---\n')
#driver = webdriver.Chrome() #--Only use this line if you are working in windows
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4') #must start driver with chromedriver 4

#Go to Tours page
driver.get("http://rest.caftest.org/tours")
print('\nRetrieving all Images on Tours Page\n')


tourImages = driver.find_elements_by_tag_name('img')
for image in tourImages:
  print(image.get_attribute('src'))
  picSize = image.size
  print(picSize)
  





#--------------------------------


#--------------------------------


time.sleep(10)

driver.close()
