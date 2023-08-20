from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLogin:

    url = 'http://demostore.supersqa.com/my-account/'
    invalid_email='abc@gmail.com'
    expected_message='Error: The password you entered for the email address abc@gmail.com is incorrect. Lost your password?'
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        self.driver.find_element(By.ID,'username').send_keys(self.invalid_email)

    def input_password(self):
        self.driver.find_element(By.ID, 'password').send_keys('abcderge')

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'[name="login"]').click()

    def verify_error_message(self):
        error_element= self.driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/ul/li')
        displayed_error=error_element.text
        assert displayed_error==self.expected_message, 'Wrong Error'

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        # self.driver.quit()

if __name__ == '__main__':
    obj=InvalidUserLogin()
    obj.main()
