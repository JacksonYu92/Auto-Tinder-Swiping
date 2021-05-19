from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import time

facebook = os.environ["FACEBOOK"]
password = os.environ["PASSWORD"]

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="q-1636318104"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()

time.sleep(4)
facebook_btn = driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook_btn.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element_by_id("email")
email_input.send_keys(facebook)
password_input = driver.find_element_by_id("pass")
password_input.send_keys(password)
login_btn = driver.find_element_by_id("loginbutton")
login_btn.click()

driver.switch_to.window(base_window)
time.sleep(4)
location_allow_btn = driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/div/div/div[3]/button[1]/span')
location_allow_btn.click()
notification_btn = driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/div/div/div[3]/button[1]/span')
notification_btn.click()
cookies_btn = driver.find_element_by_xpath('//*[@id="q-1636318104"]/div/div[2]/div/div/div[1]/button/span')
cookies_btn.click()
time.sleep(4)
later_btn = driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/div/div[3]/button[2]/span')
later_btn.click()

time.sleep(3)

for n in range(100):
    time.sleep(2)
    try:
        dislike_btn = driver.find_element_by_xpath(
            '//*[@id="q-1636318104"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button/span/svg')
        base_window.click()
        time.sleep(2)
        base_window.send_keys(Keys.ARROW_LEFT)
        base_window.send_keys(Keys.LEFT)
    except NoSuchElementException:
        continue

