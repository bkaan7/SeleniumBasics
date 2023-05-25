import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://eksisozluk1923.com") #eksi sozluge gir

driver.find_element(By.ID,"search-textbox").send_keys("selenium") # arama kutusuna selenium yaz

driver.find_element(By.XPATH,'//*[@id="search-form"]/button').click() # arama butonuna tikla
time.sleep(1) # 1 saniye bekle
driver.find_element(By.XPATH,'//*[@id="topic"]/div[1]/div[1]/span/a[1]').click() # arama tamamlandıktan sonra şükela:tümü butonuna tıkla ve en beğenilen içerikleri listele
