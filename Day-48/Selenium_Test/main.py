from selenium import webdriver

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)

driver.quit()
