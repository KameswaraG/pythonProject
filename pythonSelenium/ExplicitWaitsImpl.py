import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
for products in results:
    actualList.append(products.find_element(By.XPATH, "h4").text)
    products.find_element(By.XPATH, "div/button").click()

print(actualList)
assert expectedList == actualList
driver.find_element(By.CLASS_NAME, "cart-icon").click()
checkoutText = driver.find_element(By.CSS_SELECTOR,
                                   "div[class='cart-preview active'] div[class='action-block'] button").text
print(checkoutText)
assert checkoutText == "PROCEED TO CHECKOUT"
driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] div[class='action-block'] button").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.visibility_of(driver.find_element(By.CSS_SELECTOR, ".promoInfo")))
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
# wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, ".promoInfo"))

# Calculating total

amountList = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amount in amountList:
    sum += int(amount.text)
print(sum)
assert int(driver.find_element(By.CLASS_NAME, "totAmt").text) == sum

assert float(driver.find_element(By.CLASS_NAME, "discountAmt").text) <= int(
    driver.find_element(By.CLASS_NAME, "totAmt").text)
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"
