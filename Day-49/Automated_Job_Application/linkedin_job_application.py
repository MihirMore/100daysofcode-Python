from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=2576408054&f_AL=true&keywords=python%20developer"
ACCOUNT_EMAIL = "YOUR EMAIL"
ACCOUNT_PASSWORD = "YOUR PASSWORD"

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
driver.maximize_window()

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(3)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
save_button = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/span/button")
save_button.send_keys(Keys.ENTER)

