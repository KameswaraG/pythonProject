from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_config = Service()
driver = webdriver.Chrome(service=service_config, options=options)
driver.maximize_window()    
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

# Filling the form

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter your email address']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
