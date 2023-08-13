from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get('file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Waits/page_with_slow_image.html')
# tes=driver.find_element(By.ID,'the_slow_image')  #contoh 1
# tes=driver.find_element(By.CSS_SELECTOR,"#slow_load #the_slow_image")  #contoh 2
# tes=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.ID,'the_slow_image')))
tes=wait.until(EC.visibility_of_all_elements_located((By.ID,'the_slow_image')))
if tes:
    print("KETEMU")












# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# driver.get('file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Waits/page_with_slow_image.html')
# my_image = driver.find_element('id', 'the_slow_image')
# my_image.click()
# print("Found image")
















# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
#
# driver.get('file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Waits/page_with_slow_image.html')
#
# # my_image = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))
#
# my_image = wait.until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))
#
# print("Found image")