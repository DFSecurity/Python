
# coding: UTF-8

# gap40.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

os.system ('cls')

def main ():

    chrome_options = Options ()
    chrome_options.add_argument ('--app=https://asserth.gap40.com.br/')
    chrome_options.add_argument ('--disable-prompt-on-repost')
    chrome_options.add_argument ('--incognito')
    chrome_options.add_argument ('--disable-geolocation')

    driver = webdriver.Chrome (options = chrome_options)
    driver.maximize_window ()

    time.sleep (2.5)

    try:
    
        element = driver.find_element (By.XPATH, '//*[@id="cboCampo"]/option[3]')
        element.click ()
        
    except Exception as e:
    
        exit ()

    time.sleep(0.5)
    
    try:
    
        element = driver.find_element (By.XPATH, '//*[@id="txtValor"]')
        element.click ()
        time.sleep (1.5)
        element.send_keys ('12345678910')
        
    except Exception as e:
    
        exit ()
        
    time.sleep (1.5)

    try:
    
        element = driver.find_element (By.XPATH, '//*[@id="txtSENHA"]')
        element.click ()
        time.sleep (1.5)
        element.send_keys ('12345678910')
        
    except Exception as e:
    
        exit ()

    time.sleep (1.5)
    
    cookies = driver.get_cookies ()
    second_cookie_captured = cookies [1] ['value']

    try:
    
        element = driver.find_element (By.XPATH, '//*[@id="captchacode"]')
        element.click ()
        time.sleep (1.5)
        element.send_keys ('{}'.format (second_cookie_captured))
        
    except Exception as e:
    
        exit ()

    time.sleep (1.5)

    try:
    
        element = driver.find_element (By.XPATH, '//*[@id="btOk"]')
        element.click ()
        
    except Exception as e:
    
        exit ()

    time.sleep (5.5)
    os.system ('cls')

    driver.quit ()

if __name__ == '__main__':

    main ()