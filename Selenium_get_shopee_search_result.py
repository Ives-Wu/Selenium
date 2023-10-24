from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas
import json

import time

class select_:
    def __init__(driver_path,URL,cookies_path):
        options = Options()
        options.edge_executable_path=driver_path
        
        # This part is used to configure the behavior of the Chrome browser instance.
        # Options is a Python variable or object that holds various configuration settings for the browser.
        # By passing options=options, you are using the configuration settings stored in the options object to customize the behavior of the Chrome browser.
        driver = webdriver.Chrome(options=options)

        # Set browser size to prevent any element we need is out of range.
        driver.set_window_size(1200, 1400)
        driver.get(URL)

        # Download cookies by "EditThisCookies" extension and the cookies need to be processed by "process_cookies.py"
        with open(cookies_path, 'r') as f: 
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh() # Refresh web page to make sure cookies load correctly
        time.sleep(3)

        return driver

    # When searching for elements using Selenium, you may encounter elements like 'shadow-root' that cannot be accessed with the 'find_element' method.
    # A solution is to use JavaScript for interaction. Selenium has built-in functionality for executing JavaScript code.    
    def closs_popup(driver):
        driver.execute_script('document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector(".shopee-popup__close-btn").click()')
    
    # Simulate search something.
    def search(driver,key_words):
        search_box = driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input") 
        search_box.send_keys(key_words)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
    
    # Load price and title of merchandises as DataFrame. Variable 'page' means how many pages you want to load.
    def get_merchandise_and_price(driver,page):
        name_list,price_list = [],[]

        for i in range(page):
            driver.execute_script("window.scrollTo(0, 0);") # Make sure every beginning is from the top of the wab page.
            time.sleep(1)
            for scroll in range(5): # Try to simulate user scroll down the page, 5 times scrolling to the end of the wab page.
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight*"+str(scroll+1)+"/5);")
                time.sleep(1)
            
            name = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ie3A+n bM+7UW Cve6sh']")))
            #name = driver.find_elements(By.XPATH,"//div[@class='ie3A+n bM+7UW Cve6sh']")
        
            for n in name:
                n = str(n.text)
                name_list.append(n)

            price = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='vioxXd rVLWG6']")))
            #price = driver.find_elements(By.XPATH,"//div[@class='vioxXd rVLWG6']")
        
            for p in price:
                p = str(p.text)
                price_list.append(p)

            driver.find_element(By.XPATH, "//a[@class='shopee-icon-button shopee-icon-button--right']").click() # Click next page button

        df = pandas.DataFrame({"Title": name_list, "Price": price_list}) # Save as DataFrame

        return df


test1 = select_.__init__("C:/Users/Ives/Downloads/Webdriver/chromedriver.exe","https://shopee.tw/",'C:/Program Files/Python3/My_Python_Project/1023cookies.txt')
select_.search(test1,"iPhone15")
print(select_.get_merchandise_and_price(test1,3))