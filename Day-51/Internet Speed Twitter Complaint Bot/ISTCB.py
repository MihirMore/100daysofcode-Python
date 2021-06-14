from selenium import webdriver

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

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
