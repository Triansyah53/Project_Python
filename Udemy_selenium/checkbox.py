#D:\Udemy\SQA\Project_Python\my_code\python-selenium-course-material\python_selenium_course_material\SELENIUM_SECTION\Checkboxes\checkbox_example.html
import time
from WebDriverManager2 import create_driver
# file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Checkboxes/checkbox_example.html
from WebDriverManager2 import create_driver
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
url='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Checkboxes/checkbox_example.html'
driver.get(url)

# value = '61'
# locator = f'[value*="{value}"]'
# choice = driver.find_element(By.CSS_SELECTOR, locator)
# print("Element found")
# choice.click()
# print("Element clicked")
#
# clicked_value = choice.get_attribute('value')  # Get the value attribute of the clicked element
# assert choice.is_selected() and clicked_value == value, f"Clicked element is not selected or value doesn't match expected value '{value}'"
# print("Assertion passed")

expected=4
all_checkbox=driver.find_elements(By.NAME,'age-group-checkbox')
assert expected==len(all_checkbox),f'lol'

for checkbox in all_checkbox:
    checkbox.click()
    value=checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f'{value} is selected')
    else:
        raise Exception (f'{value} is not selected')