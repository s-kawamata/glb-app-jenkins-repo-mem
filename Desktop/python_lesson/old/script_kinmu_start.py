from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select


CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(CHROMEDRIVER)
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')
 
driver.find_element_by_xpath('//*[@id="username"]').send_keys("k_fujihira@ap-com.co.jp")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("613457Frontier")

driver.find_element_by_xpath('//*[@id="Login"]').click()

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()

driver.implicitly_wait(5)

#クリック
elements = driver.find_element_by_xpath('//*[@id="dateRow2022-10-03"]/td[7]')
#elements = driver.find_elements_by_class_name('day_tele0')
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x,y)
actions.click()
actions.perform()

driver.implicitly_wait(5)



#要素を指定する
element = driver.find_element_by_xpath('//*[@id="workLocationId"]')

driver.implicitly_wait(5)

#Selectクラスのインスタンスを生成することで様々な処理を扱える
select = Select(element)

driver.implicitly_wait(5)

#value属性の値を引数に指定することで、選択する
select.select_by_value('a2B5F00000OkMUPUA3')

#登録ボタンクリック
driver.find_element_by_xpath('//*[@id="dlgInpTimeOk"]').click()




#勤務場所をクリック
#driver.find_element_by_xpath('//*[@id="dateRow2022-09-01"]/td[7]/div/div').click()

#勤務場所ラベルをクリック
#driver.find_element_by_xpath('//*[@id="workLocationId"]').click()

#勤務場所をクリック
#driver.find_element_by_xpath('//*[@id="workLocationId"]/option[3]').click()


#driver.quit()