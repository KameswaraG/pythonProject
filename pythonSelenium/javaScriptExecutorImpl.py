from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")
service_config = Service()
driver = webdriver.Chrome(service=service_config,options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,500)")
driver.get_screenshot_as_png()
driver.get_screenshot_as_file("james.png")