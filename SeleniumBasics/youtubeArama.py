from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com") #youtube'a gir
aramaKutusu = driver.find_element(By.ID,"search-input").click() #arama kutusuna tikla
arama = driver.find_element(By.NAME,"search_query").send_keys("game of thrones") #arama kutusuna "game of thrones" yazdir
driver.find_element(By.ID,"search-icon-legacy").click() # arama butonuna tikla
driver.save_screenshot("save.png") #arama sonucunu png dosyasi olarak screenshot alip kaydet

