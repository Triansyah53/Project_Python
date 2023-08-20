import pdb
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartActions:
    coupon_verify_message = 'Coupon code applied successfully.'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def add_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.count:nth-child(2)'), '1 item'))

    def click_cart_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, 'li:first-child > a[href*="demostore.supersqa.com/cart"]').click()

    def input_coupon_and_enter(self):
        # pdb.set_trace()
        coupon_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
        driver.find_element(By.XPATH, '//*[@id="shipping_method_0_local_pickup3"]').click()
        time.sleep(1)
        coupon_input.send_keys(coupon_code, Keys.ENTER)

        # verify_element = self.driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/div')
        # verify = verify_element.text
        # assert verify == self.coupon_verify_message, 'Wrong'

    def verify_total_is_zero(self):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi'), '$0.00'))

    def main(self):
        self.add_to_cart()
        self.click_cart_menu()
        self.input_coupon_and_enter()
        self.verify_total_is_zero()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('http://demostore.supersqa.com')
    coupon_code = 'SSQA100'
    cart_actions = CartActions(driver)
    cart_actions.main()
