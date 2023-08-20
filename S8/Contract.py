from Test_Login import login
from WebDriverManager import create_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=create_driver()
login(driver)
wait=WebDriverWait(driver,3)
input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][aria-autocomplete="list"]')
input_element.send_keys("PT AGRINDO")
time.sleep(1)
input_element.send_keys(Keys.ARROW_DOWN)
input_element.send_keys(Keys.ENTER)
