import datetime
import time

#import chromedriver_binary
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait

import user_info

# # ドライバー指定でChromeブラウザを開く
# CHROMEDRIVER = "C:\chromedriver.exe"
# driver = webdriver.Chrome(CHROMEDRIVER)

# driver = webdriver.Remote(
#      command_executor="http://selenium:4444/wd/hub",
#      desired_capabilities=DesiredCapabilities.CHROME.copy(),
#  )

# #ウインドウサイズを変更
# driver.set_window_size(1920,1080)

# # Googleアクセス
# driver.get('https://login.salesforce.com/?locale=jp')

# #ログイン開始
# try:
#   #ログイン画面にてクレデンシャルを入力
#   driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_info.salesforce_id)
#   driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_info.salesforce_passwd)
#   #ログインボタンをクリック
#   driver.find_element_by_xpath('//*[@id="Login"]').click()
#   time.sleep(5)

#   #指定したdriverに対して最大で10秒間待つように設定する
#   wait = WebDriverWait(driver, 120)
#   wait.until(expected_conditions.invisibility_of_element_located((By.ID, "//*[contains(text(), 'モバイルデバイスを確認')]")))
#   time.sleep(5)
#   #指定された要素が非表示になるまで待機する(要素は約5秒後に非表示になる)
#   elm = driver.find_element_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
#   if elm :
#     pass 
#   else :
#     raise ValueError("ログインに失敗しました")
# except NoSuchElementException as e:
#   print(e)

# print("ログイン完了しました")
# time.sleep(10)

# Firefox
options = Options()
firefox_profile = "./zcy7yqlt.default-release-1679651078178" #Firefoxのprofileのパスを指定
fp = webdriver.FirefoxProfile(firefox_profile)
options.headless = True
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
driver = webdriver.Firefox(options=options,firefox_profile=fp,capabilities=firefox_capabilities)
driver.set_window_size(1920, 1080)

# Googleアクセス
driver.get('https://www.google.com/?hl=ja')

#ログイン開始
try:
  #ここからSSO処理
  time.sleep(5)
  elm = driver.find_element_by_xpath("//*[@class='gb_e']")
  actions = ActionChains(driver)
  actions.move_to_element(elm)
  actions.perform()
  actions.reset_actions()
  driver.find_element_by_xpath("//*[@aria-label='Google アプリ']").click()

  time.sleep(5)
  iframe = driver.find_element_by_xpath("//iframe[@role='presentation']")
  driver.switch_to.frame(iframe)
  time.sleep(5)
  elm = driver.find_element_by_xpath("//*[contains(text(), 'TeamSpirit')]")
  driver.execute_script("window.scrollTo(0, " + str(elm.location['y']) + ");")
  driver.find_element_by_xpath("//*[contains(text(), 'TeamSpirit')]").click()
  time.sleep(5)
  handle_array = driver.window_handles
  driver.switch_to.window(handle_array[1])
  
  #お知らせウィンドウが開いていた場合は閉じる
  notification_window = driver.find_elements_by_xpath("//div[@data-dojo-attach-point='titleBar']/*[contains(text(), 'お知らせ')]")
  
  if notification_window:
    y_loca = driver.find_element_by_xpath("//tr[@id='dialogInfoBottom']//button[@class='std-button2 close_button']")
    driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
    y_loca.click()
  else:
    pass
    
  time.sleep(5)
  elm = driver.find_elements_by_xpath("//a[@title='勤務表タブ']")
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")

except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(7)

print("処理開始します。")

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()
driver.implicitly_wait(5)

#繰り返し処理を開始
i=0
content = driver.find_elements_by_css_selector('.tele')
days = len(content)

while i < days:
    print("処理スタート")

    #日付の欄まで縦スクロール、クリック
    elements = driver.find_elements_by_css_selector('.tele')[i]
    driver.execute_script("window.scrollTo(0, " + str(elements.location['y']) + ");")
    elements.click()
    time.sleep(5)

    print("日時が選択されました")

    #「勤務場所」入力欄まで移動
    kinmu_place = driver.find_element_by_xpath('//*[@id="workLocationId"]')
    driver.execute_script("window.scrollTo(0, " + str(kinmu_place.location['y']) + ");")

    #「勤務場所」から「在宅勤務」を選択する
    select = Select(kinmu_place)
    select.select_by_value('a2B5F00000OkMUPUA3')

    #登録ボタンクリック
    driver.find_element_by_xpath('//*[@id="dlgInpTimeOk"]').click()
    i+=1
    print("登録ボタンが押されました")

    time.sleep(5)

else:
#処理対象が存在しない時の処理
#完了処理
    print("処理が正常に完了しました。")
    driver.quit()
