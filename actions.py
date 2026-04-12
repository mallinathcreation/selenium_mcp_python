from selenium.webdriver.common.by import By
from browser import start_browser

driver = None

def open_browser():
    global driver
    if not driver:
        driver = start_browser()
    return driver

def open_google():
    driver = open_browser()
    driver.get("https://www.google.com")

def search_google(query):
    driver = open_browser()
    box = driver.find_element(By.NAME, "q")
    box.send_keys(query)
    box.submit()

def open_make_my_trip():
    driver = open_browser()
    driver.get("https://www.makemytrip.com")

def close_browser():
    global driver
    if driver:
        driver.quit()
        driver = None
        return "Browser closed"
    return "No browser open"