from selenium import webdriver

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element_by_xpath("//*[@id=\"site-map\"]/div[2]/div/ul/li[3]/a")
print(bug_link.text)

driver.quit()
