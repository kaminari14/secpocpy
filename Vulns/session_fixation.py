import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def session_fixation(config):

    print('[+] Starting test for Session Fixation')

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

    base_reusables.take_screenshot('Session_Fixation/', '1-login-first.png', config, 2)

    #get-cookies
    cookies = browser.get_cookies()
    
    login_info = config['login']

    #add cookies to incognito
    browser2 = webdriver_reusables.initialise_webdriver(config, ops=['--incognito'])
    browser2.get(login_info.get('url'))
    for cookie in cookies:
        browser2.add_cookie(cookie_dict=cookie)

        

    pyautogui.keyDown('shiftleft')
    pyautogui.press('shiftright')
    pyautogui.press('f9')
    pyautogui.keyUp('shiftleft')
    time.sleep(2)
    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')

    time.sleep(2)
    base_reusables.take_screenshot('Session_Fixation/', 'add_cookies_to_new_session.png', config)

    #login
    
    webdriver_reusables.login(browser2, login_info.get('username2'), login_info.get('pass2'), config, open_url=False)
    time.sleep(2)
    base_reusables.take_screenshot('Session_Fixation/', 'refresh_browser1.png', config)    
    browser2.minimize_window()
    #refresh browser1
    browser.refresh()
    time.sleep(5)
    base_reusables.take_screenshot('Session_Fixation/', 'refresh_browser1.png', config)

    webdriver_reusables.logout(browser, config)
    webdriver_reusables.logout(browser2, config)

    browser2.quit()
    browser.quit()

    print('Finished')