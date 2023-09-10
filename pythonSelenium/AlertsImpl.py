from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config=Service()
driver=webdriver.Chrome(service=service_config)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="Kamesh"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()