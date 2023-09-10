from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_config = Service()
driver = webdriver.Chrome(service=service_config)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

actions=ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
