from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas

import time

options = Options()
options.edge_executable_path="C:/Users/Ives/Downloads/Webdriver/chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get("https://shopee.tw/")
time.sleep(3)

driver.execute_script('document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector(".shopee-popup__close-btn").click()') #關閉廣告popup
"""""
使用selenium搜尋element的時候有時候會遇到shadow-root這種element 無法使用find_element來取得物件 解法是可以使用javascript去點擊 selenium內建的function是可以call javascript的
"""""
time.sleep(3)

login = driver.find_element(By.LINK_TEXT,"登入") #定位並點擊登入按鈕
login.click()
time.sleep(3)

account = driver.find_element(By.NAME,"loginKey") #定位帳號輸入處
pw = driver.find_element(By.NAME,"password") #定位密碼輸入處

account.send_keys("X")
pw.send_keys("X")
pw.send_keys(Keys.RETURN) #需先手動登入一次 初次登入會跳出要寄簡訊驗證碼
time.sleep(3)

search_box = driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input") #搜尋s23
search_box.send_keys("S23")
search_box.send_keys(Keys.RETURN)

name_list,price_list = [],[]

for i in range(3):
    time.sleep(2.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    
    name = driver.find_elements(By.XPATH,"//div[@class='ie3A+n bM+7UW Cve6sh']") #列出商品名稱
    for n in name:
        n = str(n.text)
        name_list.append(n)

    price = driver.find_elements(By.XPATH,"//div[@class='vioxXd rVLWG6']") #列出商品價格
    for p in price:  #price_list = [p.text for p in price]
        p = str(p.text)
        price_list.append(p)

    driver.find_element(By.CSS_SELECTOR, 'svg.shopee-svg-icon.icon-arrow-right').click()
    driver.find_element(By.XPATH,"//@")

df = pandas.DataFrame({"Title": name_list, "Price": price_list})

print(df)
