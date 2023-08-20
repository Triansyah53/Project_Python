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
driver.get('https://www.shafiq.id/daftar-investasi')
wait=WebDriverWait(driver,3)

driver.find_element(By.CSS_SELECTOR,'i.icon-filter').click()
driver.find_element(By.XPATH,'//label[contains(text(),"Saham")]').click()
driver.find_element(By.XPATH,'//label[contains(text(),"Pertanian")]').click()
driver.find_element(By.XPATH,'//label[contains(text(),"Masa Kampanye")]').click()
driver.find_element(By.CSS_SELECTOR,'.btn.btn-block.btn-primary').click() #Button Terapkan
driver.find_element(By.CSS_SELECTOR,'#modal-filter-investasi .transparent-btn').click()
pdb.set_trace()