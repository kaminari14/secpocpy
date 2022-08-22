import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def concurrent_sessions(config):

    print('[+] Starting test for Concurrent Sessions')

    browser1 = webdriver_reusables.initialise_webdriver(config)
    webdriver_reusables.login(browser1, None, None, config)

    pyautogui.keyDown('winleft')
    pyautogui.press('left')
    pyautogui.keyUp('winleft')

    browser2 = webdriver_reusables.initialise_webdriver(config)
    webdriver_reusables.login(browser2, None, None, config)

    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')

    browser1.refresh()
    browser2.refresh()

    time.sleep(1)
    base_reusables.take_screenshot('Concurrennt_Sessions/', 'Concurrent_sessions.png', config)

    webdriver_reusables.logout(browser1, config)
    webdriver_reusables.logout(browser2, config)

    browser1.quit()
    browser2.quit()
    
    print('Finished')
