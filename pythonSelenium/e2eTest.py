import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_options = Service()
driver = webdriver.Chrome(service=service_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(.,'Shop')]").click()
items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for item in items:
    product = item.find_element(By.XPATH, "div/h4/a").text
    if product == "Blackberry":
        item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CLASS_NAME, "btn-primary").click()
driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
# wait.until(expected_conditions.element_to_be_clickable((By.ID, "checkbox2")))
time.sleep(3)
# driver.find_element(By.ID, "checkbox2").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successMessage)
