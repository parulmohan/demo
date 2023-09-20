import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=Service_obj)

driver.get("https://rahulshettyacademy.com/client")
t = 0.5
time.sleep(t)
