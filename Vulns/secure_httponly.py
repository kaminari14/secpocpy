from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from reusables import base_reusables, webdriver_reusables, os_reusables
import pyautogui

def httponly_secure(config):

    print('[+] Starting test for Secure HTTPOnly Flags')

    base_config = config['application_data']
    browser = webdriver_reusables.initialise_webdriver(config)
    browser.get(base_config.get('url'))
    time.sleep(3)

    webdriver_reusables.login(browser, None, None, config)

    pyautogui.keyDown('shiftleft')
    pyautogui.press('shiftright')
    pyautogui.press('f9')
    pyautogui.keyUp('shiftleft')
    
    time.sleep(2)

    base_reusables.take_screenshot('httponly_secure/','Secure_httponly1.png', config)
    browser.quit()

    print('Finished')