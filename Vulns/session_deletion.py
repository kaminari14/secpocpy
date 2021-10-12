from reusables import base_reusables, webdriver_reusables
import pyautogui
import time
from configparser import RawConfigParser

def session_deletion(config_file):
    base_config = base_reusables.get_config_data('base', config_file)
    browser = webdriver_reusables.initialise_webdriver()


    #login
    webdriver_reusables.login(browser, None, None, config_file)
    pyautogui.keyDown('shiftleft')
    pyautogui.press('shiftright')
    pyautogui.press('f9')
    pyautogui.keyUp('shiftleft')
    time.sleep(2)
    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')

    base_reusables.take_screenshot('Session_Deletion/', '1-login.png', config_file, 2)

    #get-cookies
    cookies = browser.get_cookies()
    print(cookies)

    #logout
    webdriver_reusables.logout(browser, config_file)
    base_reusables.take_screenshot('Session_Deletion/', '2-logout.png', config_file, 2)

    browser.quit()
    
    #add the cookies
    browser = webdriver_reusables.initialise_webdriver()
    browser.delete_all_cookies()
    browser.get(base_config.get('url'))
    for cookie in cookies:
        browser.add_cookie(cookie_dict=cookie)

    pyautogui.keyDown('shiftleft')
    pyautogui.press('shiftright')
    pyautogui.press('f9')
    pyautogui.keyUp('shiftleft')
    time.sleep(2)
    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')
    base_reusables.take_screenshot('Session_Deletion/', '3-cookies_added.png', config_file , 2)

    #try to access url
    login_conf = base_reusables.get_config_data('login', config_file)
    browser.get(login_conf.get('access_controlled_url'))
    base_reusables.take_screenshot('Session_Deletion/', '4-access_restricted_url.png', config_file, 5)

    browser.quit()