import time

from selenium import webdriver

driver= webdriver.Chrome()
driver_get='http://mystore.local/'
driver.get(driver_get)
time.sleep(5)