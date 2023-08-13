import time
from selenium import webdriver

driver = webdriver.Chrome()  # Make sure you have the Chrome WebDriver executable in your system PATH
driver.get("https://google.com")
time.sleep(3)
driver.quit()