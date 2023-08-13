import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

##ex1
# driver=webdriver.Chrome(options=options)
# driver.get('http://demostore.supersqa.com/my-account')
# driver.find_element(By.ID,'username').send_keys('triansyahdta2@gmail.com')
# driver.find_element(By.ID,'password').send_keys('abcd')
# driver.find_element(By.CSS_SELECTOR,'#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button').click()
#
# try:
#     warning_element=driver.find_element(By.CSS_SELECTOR,'#content > div > div.woocommerce > ul > li')
#     warning_text=warning_element.text
#     if 'Unknown email ' in warning_text:
#         print('Failed')
#     else:
#         print('Success')
# except:
#     print("Success")

##ex2

# driver = webdriver.Chrome(options=options)
# driver.get('http://demostore.supersqa.com')
#
# search = driver.find_element(By.ID, 'woocommerce-product-search-field-0').send_keys('album',Keys.ENTER)

# driver.quit()


##ex3
driver=webdriver.Chrome(options=options)
driver.get('http://demostore.supersqa.com/my-account')
driver.find_element(By.ID,'username').send_keys('admin',Keys.TAB,'admin')
