from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME,"blinkingText").click()
openBrowser= driver.window_handles
print(openBrowser)
driver.switch_to.window(openBrowser[1])
contactUs=driver.find_element(By.CSS_SELECTOR,".red").text
print(contactUs)
dir=contactUs.split("at ")[1].strip().split(" ")[0]
print(dir)