import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = "afterhours.ig"
PASSWORD = "@ft€₹h0ur$97"
CHROME_DRIVER_PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "spotifypodcasts/"


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
        time.sleep(5)
        close_popup = self.driver.find_element_by_css_selector('.mt3GC .HoLwm')
        close_popup.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        time.sleep(4)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(1):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element_by_css_selector("li button")
        print(all_buttons)
        for button in all_buttons:
            if button.text != "Follow":
                pass
            else:
                button.click()
                time.sleep(2)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
