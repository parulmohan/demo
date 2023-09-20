import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
# exception for sleep here
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
#list of web elements (plural)
count = len(results)
assert count == 3
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    #time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
#time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(10)
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
