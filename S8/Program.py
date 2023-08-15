import pdb

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from WebDriverManager import create_driver
import time
from Login import login

driver = create_driver()
login(driver)
wait=WebDriverWait(driver,3)

# Find the dosctore element and type "PT AGRINDO"
input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][aria-autocomplete="list"]')
input_element.send_keys("PT AGRINDO")
time.sleep(1)
input_element.send_keys(Keys.ARROW_DOWN)
input_element.send_keys(Keys.ENTER)

time.sleep(3)
# Klik administration
main_menu_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link.nav-dropdown-toggle')))
main_menu_link.click()

# Wait for the "Program Management" link to be clickable
program_management_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                 '#root > div > div > div > div > div > ul > li.nav-item.nav-dropdown.open > ul > li:nth-child(5) > a')))
program_management_link.click()

#click add
time.sleep(1)
add_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary i.fa-plus')
add_button.click()


time.sleep(1)
prog_name=driver.find_element(By.NAME,'name').send_keys('Dummy')
prog_desc=driver.find_element(By.NAME,'description').send_keys('Dummy Desc')

dropdown = driver.find_element(By.CSS_SELECTOR, "div.css-1wa3eu0-placeholder").click()


#Choose IDR
driver.find_element(By.CSS_SELECTOR,'#react-select-5-input').send_keys("IDR",Keys.ENTER)

#click slider Collaboration,Buyer,Multiple Buyer,Seller
enabuy=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[1]/form/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[1]/label/span').click()
multibuy=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[1]/form/div/div[1]/div[2]/div/div/table/tbody/tr[2]/td[2]/label/span').click()
enasel=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[1]/form/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/label/span').click()
time.sleep(1)
collab=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[4]/div[2]/div/div[2]/label/span').click()

#Quote
q_ena=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/label/span').click()
q_liti=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]/label/span').click()
q_invcheck=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[3]/td[2]/label/span').click()
q_lir=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td[2]/label/span').click()
q_disaprov=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/label/span').click()
q_pricecor=

q_logo = driver.find_element(By.ID, 'react-select-6-input')
q_logo.click()
q_logo.send_keys('b', Keys.ENTER)


#Order
ord=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[1]/ul/li[2]/div').click()
o_ena=driver.find_element()
o_liti=driver.find_element()
o_logo=driver.find_element()

#DA
da_pda=driver.find_element()
da_pad
da_dgc
da_sig

#RA

#INV

# XXX=driver.find_element(By.XPATH,'')
