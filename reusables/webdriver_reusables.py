from selenium import webdriver
from reusables import base_reusables
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def initialise_webdriver():
    options = webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile(r'/home/kaminari/.mozilla/firefox/kv1gy9hd.WebPTAutomation')
    browser = webdriver.Firefox(executable_path='./drivers/geckodriver', firefox_profile=profile)
    browser.implicitly_wait(10)
    browser.maximize_window()
    return  browser


def login(browser, username, password, config_file):
    try:
        login_info = base_reusables.get_config_data('login', config_file)
        browser.get(login_info.get('url'))
        username_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('username_css'))))
        password_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('password_css'))))
        submit_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('submit_css'))))
        username_btn.send_keys(username if username else login_info.get('username'))
        password_btn.send_keys(password if password else login_info.get('password'))
        submit_btn.click()
    except Exception as e:
        print(e)
        print('Something went wrong with Login functionality')


def logout(browser, config_file):
    try:
        login_info = base_reusables.get_config_data('login', config_file)
        for button in login_info.get('logout_css').split(','):
            logout_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, button)))
            logout_btn.click()
    except Exception as e:
        print(e)
        print('something went wrong with logout funtionality')