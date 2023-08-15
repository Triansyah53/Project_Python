from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get('http://s8.asyx.com')
    wait = WebDriverWait(driver, 10)
#asyxdummy
#asyxsupport
    driver.find_element(By.ID, 'username').send_keys('asyxsupport')
    driver.find_element(By.ID, 'password').send_keys('Asyx!4362023', Keys.ENTER)

    documents_link = wait.until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Documents'))
    )

    if documents_link.is_displayed():
        print("Login Success")
    else:
        print("Login Failed")