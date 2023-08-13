

from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Waits/page_with_slow_image.html')
my_image = driver.find_element('id', 'the_slow_image')
my_image.click()
print("Found image")