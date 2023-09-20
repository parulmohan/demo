import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=Service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# ID, Xpath, CSS selector,
t = 0.5
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Parul")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
time.sleep(t)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abcd1234")
time.sleep(t)
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(t)
# XPath: //tag-name[@attribute='value']
# CSS:  tag-name[attribute='value'] #id, .classname
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(t)
message = driver.find_element(By.CLASS_NAME, "alert").text
time.sleep(t)
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
time.sleep(t)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(t)
