from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver= webdriver.Chrome(options=options)
driver.get('http://s8.asyx.com')

driver.find_element(By.ID,'username').send_keys('asyxsupport')
driver.find_element(By.ID,'password').send_keys('Asyx!4362023',Keys.ENTER)

documents_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Documents'))
)

# Check if the Documents link is present
if documents_link.is_displayed():
    print("Login Success")
else:
    print("Login Failed")

