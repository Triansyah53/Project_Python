from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Provide the full path to chromedriver.exe
chrome_driver_path = r"C:\MybrowserPATH\chromedriver.exe"

# Set the path to the chromedriver executable using the Service class
service = Service(executable_path=chrome_driver_path)

# Create the Chrome WebDriver instance
driver = webdriver.Chrome(service=service)

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Wait for 5 seconds (you can remove this if you don't need it)
driver.implicitly_wait(5)

# Close the browser
driver.quit()