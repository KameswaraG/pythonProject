from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
openBrowser = driver.window_handles
print(openBrowser)
driver.switch_to.window(openBrowser[1])
contactUs = driver.find_element(By.CSS_SELECTOR, ".red").text
print(contactUs)
text = contactUs.split("at")[1].strip().split(" ")[0]
print(dir)
# driver.close()
driver.switch_to.window(openBrowser[0])
driver.find_element(By.ID,"username").send_keys(text)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR,"#terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)
