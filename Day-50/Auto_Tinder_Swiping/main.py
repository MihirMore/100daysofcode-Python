from selenium import webdriver
from time import sleep

FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)

login_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div["
                                            "1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login_button.click()
