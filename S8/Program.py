from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
options.add_argument("--start-maximized")
driver= webdriver.Chrome(options=options)
driver.get('http://s8.asyx.com')
wait=WebDriverWait(driver,10)


driver.find_element(By.ID,'username').send_keys('asyxsupport')
driver.find_element(By.ID,'password').send_keys('Asyx!4362023',Keys.ENTER)

documents_link = wait.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Documents'))
)

# Check if the Documents link is present
if documents_link.is_displayed():
    print("Login Success")
else:
    print("Login Failed")


#Klik docstore
# docstore= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#root > div > div > header > div > div > div > div.css-1wy0on6 > div > svg')))
# docstore.click()

# Click the dropdown
dropdown = driver.find_element(By.CSS_SELECTOR, '.css-yk16xz-control')
dropdown.click()

# Find and type "PT AGRINDO"
input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][aria-autocomplete="list"]')
input_element.send_keys("PT AGRINDO")

#
# # Klik administration
# main_menu_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link.nav-dropdown-toggle')))
# main_menu_link.click()
#
# # Wait for the "Program Management" link to be clickable
# program_management_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'programmanagement')))
# program_management_link.click()