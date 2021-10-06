import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def concurrent_sessions(config_file):
    
    browser1 = webdriver_reusables.initialise_webdriver()
    webdriver_reusables.login(browser1, None, None, config_file)

    pyautogui.keyDown('winleft')
    pyautogui.press('left')
    pyautogui.keyUp('winleft')

    browser2 = webdriver_reusables.initialise_webdriver()
    webdriver_reusables.login(browser2, None, None, config_file)

    pyautogui.keyDown('winleft')
    pyautogui.press('right')
    pyautogui.keyUp('winleft')

    time.sleep(1)
    base_reusables.take_screenshot('Concurrennt_Sessions/', 'Concurrent_sessions.png', config_file)

    browser1.quit()
    browser2.quit()
    

