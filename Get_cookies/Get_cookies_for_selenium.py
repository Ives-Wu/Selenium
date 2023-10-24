from selenium import webdriver
import time

# 目前是透過擴充套件抓cookie 但應該用selenium也可以抓 待研究



driver = webdriver.Chrome()  


driver.get("https://shopee.tw/")
time.sleep(3)

# 读取Cookies
cookies = driver.get_cookies()

# 将Cookies保存到txt文件
with open('Selenium/cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write(f"{cookie['name']}={cookie['value']}\n")
