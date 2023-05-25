from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.mynet.com/hava-durumu") #mynet hava durumuna gir

arama = driver.find_element(By.ID,("cityInput")) #input area bul
arama.click() # input area sec
arama.send_keys("Sakarya") # input'a Sakarya yazdir
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="cityInputautocomplete-list"]/div')).click() #acilan dinamik dropdown'da sakarya'yi tikla
time.sleep(2)

durum = driver.find_element(By.XPATH,('/html/body/div[10]/div[2]/div[2]')).text # acilan sayfadan sakarya'ya ait hava durumu bilgilerini al

print(durum) # acilan sayfadan sakarya'ya ait hava durumu bilgilerini yazdir.
