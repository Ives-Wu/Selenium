from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas

options = Options()
options.edge_executable_path="C:/Users/Ives/Downloads/Webdriver/chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get("https://forum.gamer.com.tw/")
time.sleep(3)
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

titles = driver.find_elements(By.CSS_SELECTOR,'a[data-gtm-page="熱門哈啦區"][data-gtm-area="主要列表"][data-gtm-service="forum"][data-gtm-link-click="點擊哈啦板"]')
titles_list, i = [],0
for t in titles:
    i = i+1
    if i % 2 == 0:
        t = str(t.text)
        titles_list.append(t)
        print(enumerate(t))


populars = driver.find_elements(By.XPATH, "//i[contains(text(), '板主：')]")
populars_list = []
for p in populars:
    p = str(p.text)
    p = p.split("　")
    populars_list.append(p)

merge_ls = []
for x,y in zip(titles_list,populars_list):
    merge_ls.append([x]+y)

df = pandas.DataFrame(merge_ls, columns=["標題","Owner","昨日人氣","昨日文章"])

print(df)

