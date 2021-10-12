import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def browser_cache(config_file):
    browser = webdriver_reusables.initialise_webdriver()
    
    webdriver_reusables.login(browser, None, None, config_file)
    base_reusables.take_screenshot('Browser_cache/','1-Loggedin.png', config_file, 5)
    
    webdriver_reusables.logout(browser, config_file)
    base_reusables.take_screenshot('Browser_cache/','2-Loggedout.png', config_file, 5)
    
    browser.back()
    time.sleep(5)
    base_reusables.take_screenshot('Browser_cache/','3-backpressed.png', config_file, 5)
    browser.quit()