import time
from decouple import config
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites import *
#to import all the functions from file we use *(astriek sign)

driver = open_browser("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
# time.sleep(5)
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
# time.sleep(5)
wait = WebDriverWait(driver, 10)
# driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class*='btn-primary']")))
element.click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys('Ind')
element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "India")))
element.click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText

