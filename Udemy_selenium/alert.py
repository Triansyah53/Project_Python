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
url='file:///D:/Udemy/SQA/Project_Python/my_code/python-selenium-course-material/python_selenium_course_material/SELENIUM_SECTION/Alerts/alerts_example.html'
driver.get(url)

# #ex1
# alert1=driver.find_element(By.CSS_SELECTOR,'#jsAlertExample button')
# alert1.click()
# my_alert1=driver.switch_to.alert
# my_alert1.accept()
# # my_alert.dismiss()

#ex2
alert2=driver.find_element(By.CSS_SELECTOR,'#jsConfirmExample button').click()
my_alert2=driver.switch_to.alert
my_alert2.accept()
response=driver.find_element(By.ID,'userResponse1').text
assert response == 'Great! You wsill love it!', 'DUMBO'

