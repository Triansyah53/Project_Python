from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver