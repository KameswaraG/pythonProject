import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(10)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "body[id='tinymce'] p").clear()
driver.find_element(By.CSS_SELECTOR, "body[id='tinymce'] p").send_keys("I am able to automate frames")
driver.switch_to.default_content()  # this will return back to default window
print(driver.find_element(By.TAG_NAME, "h3").text)
#time.sleep(10)
