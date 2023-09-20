import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
t = 0.5
time.sleep(t)
driver.get("https://phptravels.com/demo/")
time.sleep(t)
driver.find_element(By.NAME, "first_name").send_keys("Shantanu")
time.sleep(t)
driver.find_element(By.NAME, "last_name").send_keys("Kumar")
time.sleep(t)
driver.find_element(By.NAME, "business_name").send_keys("XYZ")
time.sleep(t)
id = driver.find_element(By.NAME, "email") # .send_keys("shantanumoradabad@gmail.com")
id.send_keys("shantanumoradabad@gmail.com")
# print("email: ", id.text)
# id = driver.find_element(By.NAME, "email")
print("email: ", id.get_attribute("value"))

time.sleep(t)
number1 = driver.find_element(By.XPATH, "//span[@id='numb1']")
print(dir(number1))
print("number 1 TEXT", number1.text)
print(number1)
time.sleep(t)
number2 = driver.find_element(By.XPATH, "//span[@id='numb2']")
print(number2)



