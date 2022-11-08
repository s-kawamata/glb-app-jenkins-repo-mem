import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
 

#TOKEN = 'xoxb-296963997159-3976993749254-8ungRxwqElywnPtZJz3QJ4Xn'
#CHANNEL = 'fujihira_test'

#url = "https://slack.com/api/chat.postMessage"
#headers = {"Authorization": "Bearer "+TOKEN}
#data  = {
#   'channel': CHANNEL,
#   'text': 'リモワ開始します'
#}
#r = requests.post(url, headers=headers, data=data)
#print("return ", r.json())


CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(CHROMEDRIVER)
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')
 
driver.find_element_by_xpath('//*[@id="username"]').send_keys("k_fujihira@ap-com.co.jp")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("613457Frontier")

driver.find_element_by_xpath('//*[@id="Login"]').click()
driver.find_element_by_xpath('//*[@id="btnStInput"]').click()

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()

#勤務場所をクリック
driver.find_element_by_xpath('//*[@id="dateRow2022-09-02"]/td[7]/div').click()



#driver.find_element_by_xpath('//*[@id="btnEtInput"]').click()

driver.quit()