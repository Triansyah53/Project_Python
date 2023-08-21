import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locator import Locators

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://s8.asyx.com')
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.ID, 'username').send_keys(Locators.username)
        driver.find_element(By.ID, 'password').send_keys(Locators.password, Keys.ENTER)
        documents_link = wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Documents'))
        )
        print("Login successful!")
    except Exception as e:
        print("Login failed:", str(e))

    yield driver

    # Teardown: Close the browser after the test
    driver.quit()
