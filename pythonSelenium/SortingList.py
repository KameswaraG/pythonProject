from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
sortedList = []
for food in veggies:
    sortedList.append(food.text)

print(sortedList)
mySortedList = sortedList.copy()
print(mySortedList)
mySortedList.sort()
assert sortedList == mySortedList
# print(mySortedList.sort())
# assert sortedList == mySortedList.sort()
# print(sortedList)
