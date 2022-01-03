import time
from reusables import base_reusables, webdriver_reusables
import pyautogui

def browser_cache(config):
    browser = webdriver_reusables.initialise_webdriver(config=config)
    
    webdriver_reusables.login(browser, None, None, config=config)
    base_reusables.take_screenshot('Browser_cache/','1-Loggedin.png', config, 5)
    
    webdriver_reusables.logout(browser, config)
    base_reusables.take_screenshot('Browser_cache/','2-Loggedout.png', config, 5)
    
    browser.back()
    time.sleep(5)
    base_reusables.take_screenshot('Browser_cache/','3-backpressed.png', config, 5)
    browser.quit()