from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://web.whatsapp.com")
time.sleep(10)
name = input("Gönderilecek kişi adı: ")
adet = int(input("Mesaj sayısı: "))
mesaj = input("Mesaj: ")
messageBox = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
messageBox.click()
time.sleep(3)
sendMessage = browser.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
time.sleep(3)
for i in range(0, adet):
    sendMessage.send_keys(mesaj)
    time.sleep(0.3)
    sendMessage.send_keys(Keys.RETURN)
    time.sleep(0.5)
var = input()