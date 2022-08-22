from reusables import base_reusables, webdriver_reusables
import pyautogui
import time
from configparser import RawConfigParser

def session_deletion(config):

    print('[+] Starting test for Session Deletion')

    base_config = config['application_data']
    browser = webdriver_reusables.initialise_webdriver(config)


    #login
    webdriver_reusables.login(browser, None, None, config)
    pyautogui.keyDown('shiftleft')
    pyautogui.press('shiftright')
    pyautogui.press('f9')
    pyautogui.keyUp('shiftleft')
    time.sleep(2)
    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')

    base_reusables.take_screenshot('Session_Deletion/', '1-login.png', config, 2)

    #get-cookies
    cookies = browser.get_cookies()

    #logout
    webdriver_reusables.logout(browser, config)
    base_reusables.take_screenshot('Session_Deletion/', '2-logout.png', config, 2)

    browser.quit()
    
    #add the cookies
    browser = webdriver_reusables.initialise_webdriver(config)
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
    base_reusables.take_screenshot('Session_Deletion/', '3-cookies_added.png', config , 2)

    #try to access url
    login_conf = config['login']
    browser.get(login_conf.get('access_controlled_url'))
    base_reusables.take_screenshot('Session_Deletion/', '4-access_restricted_url.png', config, 5)

    browser.quit()

    print('Finished')