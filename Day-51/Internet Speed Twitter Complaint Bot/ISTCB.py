from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 30
PROMISED_UP = 20
CHROME_DRIVER_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = "afterhoursatm@gmail.com"
TWITTER_PASSWORD = "@ft€₹h0ur$Tweet$"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(1)

        go_button = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                      "1]/a/span[4]")
        go_button.click()
        time.sleep(40)

        down_speed = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                       "3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        print(down_speed.text)
        up_speed = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                     "3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        print(up_speed.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        email = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div["
                                                  "1]/label/div/div[2]/div/input")
        password = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div["
                                                     "2]/label/div/div[2]/div/input")

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div["
                                                         "2]/form/div/div[3]/div")
        login_button.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
