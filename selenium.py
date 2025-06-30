from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/driver/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
if "Google" in driver.title:
    print("Successfully opened Google.")

time.sleep(6)
driver.quit()