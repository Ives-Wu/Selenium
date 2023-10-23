from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas
import json

import time

class select_:
    def __init__(driver_path,URL,cookies_path):
        options = Options()
        options.edge_executable_path=driver_path
        
        driver = webdriver.Chrome(options=options)
        driver.get(URL)

        # Download cookies by "EditThisCookies" extension and the cookies need to be processed by "process_cookies.py"
        with open(cookies_path, 'r') as f: 
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        time.sleep(3)

        return driver
    
    def closs_popup(driver):
        driver.execute_script('document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector(".shopee-popup__close-btn").click()')
        #"When searching for elements using Selenium, you may encounter elements like 'shadow-root' that cannot be accessed with the 'find_element' method.
        # A solution is to use JavaScript for interaction. Selenium has built-in functionality for executing JavaScript code."
    
    def search(driver,key_words):
        search_box = driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input") #搜尋s23
        search_box.send_keys(key_words)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
 

test1 = select_.__init__("C:/Users/Ives/Downloads/Webdriver/chromedriver.exe","https://shopee.tw/",'C:/Program Files/Python3/My_Python_Project/1023cookies.txt')
select_.search(test1,"s23")