
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction

import uiautomator2
import os
import time

"""""
Pre-setting, for more detail please refer README.md
1. Download Appium GUI in GitHub
2. pip install Appium-Python-Client
3. Download Appium Inspector in GitHub for check element
4. Set Android_HOME env var to where Android SDK in
5. Set JAVA_HOME env var to where JDK in
6. Install Node.js then open terminel here, try install appium via npm
7. Need to run "$appium driver install uiautomator2" in terminal to make sure there's driver
8. run "$appium  -p 4723--allow-insecure=chromedriver_autodownload" to connect appium server
"""""
# Send device info for communication
device = {
    'platformName' : 'Android',
    'platformVersion' : '11.0',
    'deviceName' : 'UDID or SN',
    'browserName' : 'Chrome',
    'chromeOptions': {'args':['--incognito', '--disable-cache']}
}


capabilities = UiAutomator2Options().load_capabilities(device) # Load options
server = 'http://localhost:4723' # Default server path
URL = 'https://www.cathaybk.com.tw/cathaybk/'
#driver_path = 'C:/Users/Ives/Downloads/Webdriver/chromedriver.exe'

def init(appium_server,device_cap): # Create communication
	driver = webdriver.Remote(appium_server, device_cap, options=capabilities)
	return driver

def open_web(driver:webdriver, url:str): # Open web
    driver.get(url)

def capture_screenshot(driver:webdriver,screenshot_path:str):
    driver.save_screenshot(screenshot_path)

def tap_menu(driver:webdriver):
    driver.find_element(By.XPATH,"//*[@class='cubre-a-burger__img -close']").click()

def go_to_card_menu(driver:webdriver):
    driver.find_element(By.XPATH,"//div[text()='產品介紹']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[text()='信用卡']").click()
    time.sleep(1)

def go_to_card_list(driver:webdriver):
    """
    Sould be executed after go_to_card_menu()
    """
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='卡片介紹']").click()
    time.sleep(1)

def go_to_page_end(driver:webdriver): # Scroll to the end to make sure every element be loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def go_to_unavaliable_card(driver:webdriver): # Scroll to the position for capture
    
    ele = driver.find_element(By.XPATH,"//div[text()='停發卡']")
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    driver.execute_script("window.scrollBy(0, -200);")

def count_unavaliable_cards(driver:webdriver): # Count unavaliable cards
    count = driver.find_elements(By.XPATH,"//div[contains(text(),'本卡已停止申辦')]") 
    return len(count)


def unavaliable_cards_screenshot(driver:webdriver,num:int):
    for n in range(num):
        driver.save_screenshot("C:/Users/Ives/Downloads/screenshot"+str(n+3)+".png")
        action = TouchAction(driver)
        action.press(x=900, y=1400).move_to(x=100, y=1400).release().perform()
        time.sleep(1)


driver = init(server, device)
print("Question1 官網首頁截圖")
open_web(driver,URL)
capture_screenshot(driver, 'C:/Users/Ives/Downloads/screenshot1.png')
print("Question2 計算信用卡列表項目並截圖")
tap_menu(driver)
go_to_card_menu(driver)
capture_screenshot(driver, 'C:/Users/Ives/Downloads/screenshot2.png')
print("Question3 計算已停用信用卡數量並截圖")
go_to_card_list(driver)
go_to_page_end(driver)
go_to_unavaliable_card(driver)
print("共"+str(count_unavaliable_cards(driver))+"張")
unavaliable_cards_screenshot(driver,10)


