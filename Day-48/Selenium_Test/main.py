from selenium import webdriver

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/JBL-Waterproof-Bluetooth-Speaker-PartyBoost/dp/B07SVH63PX/ref=sr_1_2_sspa?dchild=1&keywords=jbl+speaker&qid=1623075045&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFON1E4WU1UVzhORlQmZW5jcnlwdGVkSWQ9QTAxMTQ2MTU0VDZDSVZIWjVOV0QmZW5jcnlwdGVkQWRJZD1BMDE0NjgzMTI5TUhMMTlFTUdMUlEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

driver.quit()
