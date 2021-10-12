import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def session_fixation(config_file):
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
    pyautogui.press('left')
    pyautogui.keyUp('winleft')

    base_reusables.take_screenshot('Session_Fixation/', '1-login-first.png', config_file, 2)

    #get-cookies
    cookies = browser.get_cookies()
    
    login_info = base_reusables.get_config_data('login', config_file)

    #add cookies to incognito
    browser2 = webdriver_reusables.initialise_webdriver(['--incognito'])
    browser2.get(login_info.get('url'))
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

    time.sleep(2)
    base_reusables.take_screenshot('Session_Fixation/', 'add_cookies_to_new_session.png', config_file)

    #login
    
    webdriver_reusables.login(browser2, login_info.get('username2'), login_info.get('pass2'), config_file, open_url=False)
    time.sleep(2)
    base_reusables.take_screenshot('Session_Fixation/', 'refresh_browser1.png', config_file)    
    browser2.minimize_window()
    #refresh browser1
    browser.refresh()
    time.sleep(5)
    base_reusables.take_screenshot('Session_Fixation/', 'refresh_browser1.png', config_file)

    webdriver_reusables.logout(browser, config_file)
    webdriver_reusables.logout(browser2, config_file)

    browser2.quit()
    browser.quit()