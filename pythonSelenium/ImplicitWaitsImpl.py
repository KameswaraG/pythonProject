import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
for products in results:
    products.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CLASS_NAME, "cart-icon").click()
checkoutText = driver.find_element(By.CSS_SELECTOR,
                                   "div[class='cart-preview active'] div[class='action-block'] button").text
print(checkoutText)
assert checkoutText == "PROCEED TO CHECKOUT"
driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] div[class='action-block'] button").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"
