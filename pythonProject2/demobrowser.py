import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/parul/Documents/chromedriver_linux64")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com")
sleep_time = 2
time.sleep(sleep_time)
print(driver.title)
time.sleep(sleep_time)
print(driver.current_url)
driver.get("https://www.google.com/gmail")
time.sleep(sleep_time)
driver.minimize_window()
time.sleep(sleep_time)
driver.maximize_window()
time.sleep(sleep_time)
driver.back()
time.sleep(sleep_time)
driver.refresh()
time.sleep(sleep_time)
driver.forward()
time.sleep(sleep_time)
driver.close()
