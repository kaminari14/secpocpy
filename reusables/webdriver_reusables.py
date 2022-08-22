from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time, sys


def initialise_webdriver(config, ops = []):
    firefox_config = config['firefox']
    options = webdriver.FirefoxOptions()
    for i in ops:
        options.add_argument(i)
    if firefox_config.get('firefox_location'):
        options.binary_location = firefox_config.get('firefox_location')
    profile = webdriver.FirefoxProfile(firefox_config.get('profile_location'))
    browser = webdriver.Firefox(executable_path=firefox_config.get("webdriver_location"), firefox_profile=profile, firefox_options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    return browser


def login(browser, username, password, config, open_url = True, r=0):
    try:
        login_info = config['login']
        if open_url:
            browser.get(login_info.get('url'))
        browser.implicitly_wait(5)
        username_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('username_css'))))
        password_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('password_css'))))
        submit_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, login_info.get('submit_css'))))
        username_btn.send_keys(username if username else login_info.get('username'))
        password_btn.send_keys(password if password else login_info.get('password'))
        submit_btn.click()
    except Exception as e:
        sys.stderr.write(str(e))
        sys.stderr.write('Something went wrong with Login functionality')
        if r==0:
            login(browser, username, password, config, open_url=open_url, r=1)

def logout(browser, config):
    try:
        login_info = config['login']
        logout_url = login_info.get('logout_url')
        if logout_url:
            browser.get(logout_url)
            return True
        for button in login_info.get('logout_css').split(','):
            logout_btn = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, button)))
            logout_btn.click()
    except Exception as e:
        sys.stderr.write(str(e))
        sys.stderr.write('something went wrong with logout funtionality')