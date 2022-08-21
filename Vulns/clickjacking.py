import time
from reusables import base_reusables, webdriver_reusables, os_reusables
import os


def clickjacking(config):
    base_data = config['application_data']
    os_reusables.makedirectory('./POCs/' + base_data.get('application_name') + '/Clickjacking/')

    browser = webdriver_reusables.initialise_webdriver(config)
    path = 'POCs/' + base_data.get('application_name') + '/Clickjacking/clickjacking.html'

    with open('./HTML/clickjacking.html', 'r') as cjr:
        code = cjr.read()
    with open(path, 'w') as cjw:
        cjw.write(code.replace(r'{{url}}', base_data.get('url')))
        
    browser.get("file:///"+ os.getcwd() +"/"+ path)
    
    time.sleep(2)
    
    base_reusables.take_screenshot("Clickjacking/","Clickjacking1.png", config)
    
    browser.quit()

