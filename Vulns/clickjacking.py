import time
from reusables import base_reusables, webdriver_reusables, os_reusables
import os


def clickjacking(config):
    base_data = config['application_data']
    browser = webdriver_reusables.initialise_webdriver(config)
    with open('./HTML/clickjacking.html', 'r') as cjr:
        code = cjr.read()
    with open('./HTML/clickjacking.html', 'w') as cjw:
        cjw.write(code.replace(r'{{url}}', base_data.get('url')))
        
    browser.get("file:///"+ os.getcwd() +"/HTML/clickjacking.html")
    
    time.sleep(2)
    
    base_reusables.take_screenshot("Clickjacking/","Clickjacking1.png", config)
    
    browser.quit()

