import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

#ex1 placeholder
# search_field=driver.find_element(By.ID,'woocommerce-product-search-field-0')
# place_holder=search_field.get_attribute('placeholder')
# if place_holder !='Search products…':
#     raise Exception('Wrong placeholder')
# else:print("Correct")

#ex2 see which tab is selected
# account=driver.find_element(By.CSS_SELECTOR, 'li.page-item-9').click()
# nav_items=driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li')
#
# for item in nav_items:
#     item_class=item.get_attribute('class')
#     if 'current_page_item' in item_class:
#         print(f"the selected tab is {item.text}")

# pdb.set_trace()

#example get link url
product_link=driver.find_element(By.CSS_SELECTOR,'li.product a')
product_url=product_link.get_attribute('href')
print(product_url)