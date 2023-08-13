from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.implicitly_wait(5)
try:
# inputbpx = driver.find_element(By.NAME, 'q')
    inputbpx = driver.find_element(By.ID, 'APjFqb')
    # inputbpx = driver.find_element(By.CLASS_NAME, 'gLFyf')
    # inputbpx = driver.find_element(By.TAG_NAME, 'textarea')
    # inputbpx = driver.find_element(By.LINK_TEXT, 'Search')
    # inputbpx = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search')
    # inputbpx = driver.find_element(By.CSS_SELECTOR, '.gLFyf')
    # inputbpx = driver.find_element(By.XPATH, '//textarea[@id="APjFqb"]')

    inputbpx.send_keys('testing')
    print('find it')
except:
    print('not found')
driver.quit()

