import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = "YOUR INSTAGRAM EMAIL"
PASSWORD = "YOUR INSTAGRAM PASSWORD"
CHROME_DRIVER_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "INSTAGRAM ACCOUNT YOU WANT TO BECOME"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        username_field = self.driver.find_element_by_name("username")
        password_field = self.driver.find_element_by_name("password")
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        time.sleep(2)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
