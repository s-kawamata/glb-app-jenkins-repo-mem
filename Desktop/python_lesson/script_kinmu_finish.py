import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(CHROMEDRIVER)
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')
 
driver.find_element_by_xpath('//*[@id="username"]').send_keys("k_fujihira@ap-com.co.jp")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("613457Frontier")

driver.find_element_by_xpath('//*[@id="Login"]').click()

driver.implicitly_wait(20)
#driver.find_element_by_xpath('//*[@id="btnStInput"]').click()
driver.find_element_by_xpath('//*[@id="btnEtInput"]').click()

#driver.quit()