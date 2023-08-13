# file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Drop_Down/drop_down_example.html
import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
url = 'file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Drop_Down/drop_down_example.html'
driver.get(url)

#option 1 is using select class
# dropdown=driver.find_element(By.ID,'age-range-select')
# dropdown_object=Select(dropdown)
# dropdown_object.select_by_index(3)
# dropdown_object.select_by_value('21-40')
# all_options=dropdown_object.options
# for option in all_options:
#     print(option.text)
# pdb.set_trace()

#option2
driver.find_element(By.ID,'dropdownMenuButton').click()
dropdown_item = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dropdown-item')))
dropdown_item.click()
