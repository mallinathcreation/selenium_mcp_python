from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("Step 1: Starting script")

options = Options()
options.add_argument("--start-maximized")

print("Step 2: Creating driver")

driver = webdriver.Chrome(options=options)

print("Step 3: Opening Google")

driver.get("https://www.google.com")

time.sleep(5)

print("Step 4: Closing browser")
driver.quit()