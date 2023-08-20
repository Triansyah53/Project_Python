import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

url1='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Multiple_Windows_and_Tabs/new_page_1.html'
url2='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Multiple_Windows_and_Tabs/new_page_2.html'
url3='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Multiple_Windows_and_Tabs/windows-and_tabs_example.html'
driver.get(url3)

driver.find_element(By.CSS_SELECTOR,'[href*="page_1"]').click()
original_window=driver.current_window_handle
all_window=driver.window_handles
new_window=all_window[1]

# driver.close()
pdb.set_trace()

