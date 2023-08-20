<<<<<<< HEAD
from Test_Login import login
=======
import pdb

from Login import login
from selenium.webdriver.common.by import By
>>>>>>> 96af805a4448d4fe828ed400b60759bb8192b7f0
from WebDriverManager import create_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver=create_driver()
login(driver)
wait=WebDriverWait(driver,3)
input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][aria-autocomplete="list"]')
input_element.send_keys("PT AGRINDO")
time.sleep(1)
input_element.send_keys(Keys.ARROW_DOWN)
input_element.send_keys(Keys.ENTER)

# Klik administration
main_menu_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link.nav-dropdown-toggle')))
main_menu_link.click()

# Wait for the "Contracts" link to be clickable
contract_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="contract"]')))
contract_link.click()

#Add contract
add_contract= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'i.fa.fa-plus')))
add_contract.click()

pdb.set_trace()
