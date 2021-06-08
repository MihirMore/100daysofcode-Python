from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
number_of_articles = driver.find_element_by_css_selector("#articlecount a")
print(number_of_articles)
number_of_articles.click()

all_portals = driver.find_element_by_partial_link_text("All portals")
all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Mihir")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("More")
email = driver.find_element_by_name("email")
email.send_keys("mihirmore123@mail.com")
button = driver.find_element_by_css_selector("form button")
button.click()
