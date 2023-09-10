import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countryDropdown = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] a")
print(len(countryDropdown))

for country in countryDropdown:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
