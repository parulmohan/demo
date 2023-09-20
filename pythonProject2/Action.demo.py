import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
