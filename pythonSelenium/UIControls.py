import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()

driver = webdriver.Chrome(service=service_config)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxList=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(len(checkboxList))

for checkbox in checkboxList:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(3)
        assert checkbox.is_selected()
        break


radioList=driver.find_elements(By.CSS_SELECTOR,".radioButton")
for button in radioList:
    if button.get_attribute("value") == "radio3":
        button.click()
        assert button.is_selected()
        break

