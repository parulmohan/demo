from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def my_function():
#     print("Starting...")
#     time.sleep(10)  # Sleep for 10 seconds
#     print("Done sleeping!")
#
# # Call the function
# my_function()
def open_browser(url):
    Service_obj = Service("/home/parul/Documents/chromedriver_linux64")
    driver = webdriver.Chrome(service=Service_obj)
    driver.implicitly_wait(5)
    driver.get(url)

    return driver

def login(driver):
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys(config('USER_NAME'))
    driver.find_element(By.ID, "password").send_keys(config('PASSWORD'))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    loader_un_till_visible(driver)

def select_bucket1(driver):
    # get element  after explicitly waiting for 10 seconds
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ant-select-selection-item")))
    # click the element
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='fiq-screenshots']")))
    element.click()


def select_bucket2(driver):
    # get element  after explicitly waiting for 10 seconds
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='maskedbucketList']"))).send_keys(Keys.ENTER)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@title='forwarded'])[2]")))
    element.click()

def click_settings(driver):
    loader_un_till_visible(driver)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='menu-username' and text()='Settings']")))
    action = ActionChains(driver)
    action.move_to_element(element).click().perform()
def choose_peg(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/peg']"))).click()
    # driver.find_element(By.XPATH, "//a[@href='/peg']").click()
    # action = ActionChains(driver)
    # action.move_to_element(dropdown).click().perform()
    time.sleep(5)

def loader_un_till_visible(driver):
    try:
        wait = WebDriverWait(driver, timeout=30)
        element = By.XPATH, "//span[@class='loader-og']"
        wait.until(EC.invisibility_of_element(element))

    except:
        print('loader not visible')