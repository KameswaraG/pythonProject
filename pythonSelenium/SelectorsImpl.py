from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_config = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_config, options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"));
dropdown.select_by_index(2)
