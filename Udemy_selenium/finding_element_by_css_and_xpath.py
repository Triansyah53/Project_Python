from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("http://demostore.supersqa.com")

# cart=driver.find_element(By.CSS_SELECTOR,'#site-header-cart > li:nth-child(1) > a')
cart=driver.find_element(By.CSS_SELECTOR,'#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
cart.click()
input("")
# time.sleep(3)
