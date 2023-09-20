import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
t = 0.5
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(t)
# Xpath: // is used for sepration
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(t)
# CSS: space is used to sepration
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@123")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@123")
time.sleep(t)
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(t)
