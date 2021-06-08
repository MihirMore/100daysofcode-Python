from selenium import webdriver

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element_by_css_selector("#articlecount a")
print(number_of_articles)
# number_of_articles.click()

all_portals = driver.find_element_by_partial_link_text("All portals")
all_portals.click()

