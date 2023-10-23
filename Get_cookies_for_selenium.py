from selenium import webdriver
import time

# 初始化一个浏览器实例
driver = webdriver.Chrome()  # 或者使用其他浏览器，如Firefox

# 打开目标网站，确保在加载Cookies之前
driver.get("https://shopee.tw/")
time.sleep(3)

# 读取Cookies
cookies = driver.get_cookies()

# 将Cookies保存到txt文件
with open('Selenium/cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write(f"{cookie['name']}={cookie['value']}\n")
