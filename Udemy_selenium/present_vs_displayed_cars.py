# D:\Udemy\SQA\Project_Python\my_code\python-selenium-course-material\python_selenium_course_material\SELENIUM_SECTION\presents_vs_displayed\present_vs_visible_example_with_cars.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/presents_vs_displayed/present_vs_visible_example_with_cars.html')
driver.implicitly_wait(5)
# hidden=driver.find_element(By.CSS_SELECTOR,('#bmw-models > input[type=checkbox]:nth-child(7)'))
# hidden.click()
# hidden=WebDriverWait(driver,8).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#bmw-models > input[type=checkbox]:nth-child(7)')))
driver.find_element(By.CSS_SELECTOR,'#bmw').click() 
hidden=WebDriverWait(driver,8).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#bmw-models > input[type=checkbox]:nth-child(7)')))
