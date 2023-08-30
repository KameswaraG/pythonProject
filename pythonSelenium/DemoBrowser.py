from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Driver setup
# service_obj = Service()  # Similar to WebDriver Manager

# driver = webdriver.Chrome(service=service_obj)
# driver.get('https://pypi.org/project/selenium/')

# Setting chrome driver path manually

service_obj = Service("C:/Users/Shalini/PycharmProjects/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://pypi.org/project/selenium/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://chromedriver.chromium.org/downloads")
driver.back()
driver.forward()
driver.refresh()
driver.close()