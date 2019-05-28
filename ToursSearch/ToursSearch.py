from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional

#Set to HEADLESS Chrome Driver (UNCOMMENT BELOW LINE)
#driver = webdriver.Chrome(chrome_options=options) #un-comment for headless
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4')

#Set to Chrome Driver (UNCOMMENT BELOW LINE TO SEE BROWSER SIMULATED ACTIONS)
#driver = webdriver.Chrome()

#Go to Tours page
driver.get("http://rest.caftest.org/tours")
print('Retrieving Tours Page')

CHI_BTN_Tour = driver.find_element_by_class_name('tour_search')
driver.execute_script("arguments[0].scrollIntoView();", CHI_BTN_Tour)
print('Scrolling down to Search Area')

action = ActionChains(driver);
walkTour = driver.find_element_by_xpath('//*[@id="search"]/section/div/div[1]/div[3]/div[1]/div/button[2]')
action.move_to_element(walkTour).perform();
#walkTour.click()
time.sleep(3)
walkTour.send_keys(Keys.RETURN)

print('Navigating To Walking Tours')

print('TEST RUN SUCCESSFULLY COMPLETED')












