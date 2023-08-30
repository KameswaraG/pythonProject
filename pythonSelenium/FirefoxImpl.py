from selenium import webdriver
from selenium.webdriver.edge.service import Service

# from selenium.webdriver.firefox.service import Service

# Firefox
# service_obj=Service()
# driver=webdriver.Firefox(service=service_obj)
# driver.get("https://chromedriver.chromium.org/downloads")

#Edge
service_obj = Service()
driver = webdriver.Edge(service=service_obj)
driver.get("https://chromedriver.chromium.org/downloads")
