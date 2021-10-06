from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from reusables import base_reusables, webdriver_reusables, os_reusables
import pyautogui

def httponly_secure(config_file):
    base_config = base_reusables.get_config_data('base', config_file)
    browser = webdriver_reusables.initialise_webdriver()
    browser.get(base_config.get('url'))
    time.sleep(3)
    print(browser.get_cookies())

    webdriver_reusables.login(browser, None, None, config_file)

    pyautogui.keyDown('shift')
    pyautogui.press('f9')
    pyautogui.keyUp('shift')
    
    time.sleep(2)

    base_reusables.take_screenshot('httponly_secure/','Secure_httponly1.png', config_file)
    browser.quit()
    