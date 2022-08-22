from reusables import base_reusables, webdriver_reusables
import pyautogui

def username_enumration(config):

    print('[+] Starting test for Usernname Enumration')

    browser = webdriver_reusables.initialise_webdriver(config)
    
    #invalid User
    webdriver_reusables.login(browser, 'testasdf', 'testasdf', config)
    base_reusables.take_screenshot('Username_Enumration/','invalid_username.png', config ,3 )
    browser.quit()

    browser = webdriver_reusables.initialise_webdriver(config)
    #valid User
    webdriver_reusables.login(browser, None, 'testasdf', config)
    base_reusables.take_screenshot('Username_Enumration/','valid_username.png' ,config, 3)
    browser.quit()

    print('Finished')