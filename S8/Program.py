import pdb

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebDriverManager import create_driver
import time
from Login import login
try:
    driver = create_driver()
    login(driver)
    wait=WebDriverWait(driver,3)
    # asd=driver.find_element(By.CSS_SELECTOR, 'tbody tr td:nth-child(2) .switch-slider').click()
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
    program_management_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href*="programmanagement"]')))
    program_management_link.click()

    #click add
    time.sleep(1)
    add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary i.fa-plus')))
    add_button.click()
    pdb.set_trace()


    time.sleep(1)
    prog_name=wait.until(EC.element_to_be_clickable((By.NAME,'name')))
    prog_name.send_keys('Dummy Automation')
    prog_desc=driver.find_element(By.NAME,'description').send_keys('Dummy Desc')

    dropdown = driver.find_element(By.XPATH, '//div[contains(text(), "Type to Select")]').click()
    #Choose IDR
    driver.find_element(By.CSS_SELECTOR,'#react-select-5-input').send_keys("IDR",Keys.ENTER)
    pdb.set_trace()
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
    # q_pricecor=

    q_logo = driver.find_element(By.ID, 'react-select-6-input')
    q_logo.click()
    q_logo.send_keys('supp', Keys.ENTER)

    #Order
    ord=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[1]/ul/li[2]/div').click()
    o_ena=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/label/span').click()
    o_logo=driver.find_element(By.ID,'react-select-6-input').send_keys('supp',Keys.ENTER)
    o_liti=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]/label/span').click()

    #DA
    da=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[1]/ul/li[3]/div').click()
    da_pda=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[3]/td[2]/label/span').click()
    da_dgc=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td[2]/label/span').click()
    da_invenc=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/label/span').click()
    da_sig=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[7]/td[2]/label/span').click()
    da_addsig=driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary.btn-sm')
    da_addsig.click()
    da_addsig.click()
    da_logo=driver.find_element(By.ID,'react-select-6-input').send_keys('supp',Keys.ENTER)
    da_tesxtsig=driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > main > div.mt-4.container-fluid > div > div > div > div > div.card-body > form > div:nth-child(5) > div > div > div.tab-pane.active > div > div.row > div:nth-child(2) > div > div > table > tbody > tr:nth-child(8) > td > table > tbody > tr:nth-child(1) > td:nth-child(1) > input').send_keys('Sender',Keys.TAB,Keys.TAB,'Receiver')
    time.sleep(2)
    #RA
    driver.execute_script("window.scrollTo(0, 0);")
    ra=driver.find_element(By.CSS_SELECTOR,'li.align-items-center.list-group-item-action.list-group-item:nth-child(4) div.d-flex.w-100.justify-content-between')
    ra.click()
    ra_logo=driver.find_element(By.ID,'react-select-6-input').send_keys('buy',Keys.ENTER)


    #PI
    pi=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[1]/ul/li[5]/div').click()
    piena=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/label/span').click()

    #INV
    inv=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[1]/ul/li[6]/div').click()
    inv_sig=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div[2]/div/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/label/span').click()
    inv_addsig=driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary.btn-sm > i.fa.fa-plus')
    inv_addsig.click()
    inv_textsig=driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > main > div.mt-4.container-fluid > div > div > div > div > div.card-body > form > div:nth-child(5) > div > div > div.tab-pane.active > div > div.row > div:nth-child(2) > div > div > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(1) > input').send_keys('Board of Director')
    inv_logo=driver.find_element(By.ID,'react-select-12-input').send_keys('supp',Keys.ENTER)

    #save
    save=driver.find_element(By.ID,'btn-save-program').click()
    print('PASSED')

except Exception as e:
    print('FAILED:', str(e))