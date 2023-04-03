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

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options

import user_info

# TOKEN = user_info.slack_token
# CHANNEL = 'akatsuka_test'

# url = "https://slack.com/api/chat.postMessage"
# headers = {"Authorization": "Bearer "+TOKEN}
# data  = {
#   'channel': CHANNEL,
#   'text': 'リモワ開始します'
# }

# r = requests.post(url, headers=headers, data=data)

# if "\'ok\': True" in str(r.json()):
#   print("SlackへのPOST成功")
# else:
#   print("SlackへのPOST失敗")

# #ドライバー指定でChromeブラウザを開く
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
# print("ログイン開始します。")
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

print("勤怠登録をします。")
#iframeを切り替える
iframe=driver.find_element_by_xpath("//*[@id='0665F00000117vk']")
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)

#在宅勤務ボタンを選択
y_loca = driver.find_element_by_xpath("//*[@id='workLocationButtons']/label[2]/div")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

#出勤ボタンをクリック
y_loca = driver.find_element_by_xpath("//*[@id='btnStInput']")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

driver.switch_to.default_content()

#完了処理
print("処理が正常に完了しました。")
driver.quit()
