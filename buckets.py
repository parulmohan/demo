import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilites import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# service_obj = Service("CC:/webdriver/Chrome")
# driver = webdriver.Chrome(service=service_obj)
# driver.get(config('URL'))
from selenium.webdriver.common.action_chains import ActionChains
driver = open_browser(config('URL'))
# open browser is a 'function called' and config is an .env file
login(driver)
# driver.maximize_window()
# driver.find_element(By.ID, "username").send_keys(config('USER_NAME'))
# driver.find_element(By.ID, "password").send_keys(config('PASSWORD'))
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(4)
select_bucket1(driver)
# driver.find_element(By.CLASS_NAME, "ant-select-selection-item").click()
# time.sleep(4)
# dropdown = driver.find_element(By.XPATH, "//div[@title='fiq-screenshots']")
# dropdown.click()  # Open the dropdown
# time.sleep(10)
# options = dropdown.find_elements(By.TAG_NAME, "div")  # Assuming the options are listed as <div> tags
# time.sleep(10)
select_bucket2(driver)
# driver.find_element(By.XPATH, "//input[@id='maskedbucketList']").send_keys(Keys.ENTER)
# time.sleep(5)
# buckets = driver.find_element(By.XPATH, "(//div[@class='ant-select-item-option-content'])[10]").click()
# time.sleep(5)
click_settings(driver)
# dropdown = driver.find_element(By.XPATH, "//span[@class='menu-username' and text()='Settings']")
# action = ActionChains(driver)
# action.move_to_element(dropdown).click().perform()
# time.sleep(10)
choose_peg(driver)
# driver.find_element(By.XPATH, "//a[@href='/peg']").click()
# action = ActionChains(driver)
# action.move_to_element(dropdown).click().perform()
# time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
