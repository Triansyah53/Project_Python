import pdb
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver_get = 'http://demostore.supersqa.com/'

driver.get(driver_get)  # Open the specified URL

# Find the element with ID 'site-header-cart'
cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()
driver.get('http://demostore.supersqa.com/my-account/')
u_name=driver.find_element(By.ID,'username')
u_name.send_keys('abcd')
i_name=driver.find_element(By.ID, 'password')
i_name.send_keys('abcd')
l_name=driver.find_element(By.NAME,'login')
l_name.click()
time.sleep(10)
# Continue with your testing tasks and interactions

# Close the browser window when you're done
# driver.quit()
