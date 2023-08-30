from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=opts)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, Xpath, Name, ClassName, CSSSelector,text & Link

# Xpath Syntax : //tagName[@attribute='value']
# CSS syntax : //tagName[attribute='value']
driver.find_element(By.NAME, "email").send_keys("abc@gkc.com")
driver.find_element(By.NAME, "name").send_keys("Bravo")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Welcome123")
driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

alertText = driver.find_element(By.CLASS_NAME, "alert-success").text
print(alertText)
assert "Successor! The Form has been submitted successfully!." in alertText
