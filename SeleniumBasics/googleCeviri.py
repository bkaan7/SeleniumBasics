from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://translate.google.com")

english = driver.find_element(By.CLASS_NAME,"er8xn").send_keys("hello world")
