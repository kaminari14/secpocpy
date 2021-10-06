from reusables import base_reusables, webdriver_reusables
import pyautogui

def username_enumration(config_file):
    browser = webdriver_reusables.initialise_webdriver()
    
    #invalid User
    webdriver_reusables.login(browser, 'testasdf', 'testasdf', config_file)
    base_reusables.take_screenshot('Username_Enumration/','invalid_username.png', config_file ,3 )
    browser.quit()

    browser = webdriver_reusables.initialise_webdriver()
    #valid User
    webdriver_reusables.login(browser, None, 'testasdf', config_file)
    base_reusables.take_screenshot('Username_Enumration/','valid_username.png' ,config_file, 3)
    browser.quit()