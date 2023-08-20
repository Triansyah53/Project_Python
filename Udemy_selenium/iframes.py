from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
url1='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/iFrames/iFrames_example.html'
url2='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/iFrames/to_be_in_frame.html'
driver.get(url1)

# WebElement
# ID
# NAME
# INDEX

##ex without iframe
# driver.find_element(By.ID,'btnOutFrame').click()
# my_alert=driver.switch_to.alert
# my_alert_text=my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', 'LOL'
# my_alert.dismiss()

#$ex of iframe
my_frame=driver.find_element(By.ID,'myFrame1')
driver.switch_to.frame(my_frame)
driver.find_element(By.ID,'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

##SWITCH BACK
driver.switch_to.default_content()

# my_alert=driver.switch_to.alert
# my_alert_text=my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', 'LOL'
# my_alert.dismiss()

# using 'ID'
# driver.switch_to.frame('myFrame1')
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# Using 'Index'
# driver.switch_to.frame(2)
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()