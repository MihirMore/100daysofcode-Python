from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Opening Tinder website om chrome
driver.get("http://www.tinder.com")
# sleep of 2 seconds is set so that site is completely loaded
sleep(2)

login_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div["
                                            "1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login_button.click()
# sleep of 2 seconds is set so that site is completely loaded
sleep(2)
facebook_login_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
facebook_login_button.click()

# Now login to facebook in facebook window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login using Facebook Credentials
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
