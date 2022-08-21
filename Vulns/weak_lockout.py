import os
from reusables import base_reusables, webdriver_reusables
from datetime import datetime
import time

def weak_lockout(config):
    base_config = config['application_data']
    passwd = config['login']['password']
    np = 15
    word_list = ["TestPassword|"+str(i+1) for i in range(np)]
    result = []

    browser = webdriver_reusables.initialise_webdriver(config)

    for i in range(np+1):
        webdriver_reusables.login(browser, None, word_list[i] if i!=np else None, config)
        time.sleep(4)
        now = datetime.now().time()
        base_reusables.take_screenshot("Weak Lockout/", ("Fail" + str(i+1) + ".png") if i != np else "Pass.png", config)
        result.append([i+1, word_list[i] if i != np else passwd, (("Weak Lockout/Fail" + str(i+1) + ".png") if i != np else "Weak Lockout/Pass.png"), now])

    path = 'POCs/' + base_config.get('application_name') + '/Weak Lockout/weaklockout.html'

    with open('./HTML/weak_lockout.html', 'r') as cjr:
        code = cjr.read()
    with open(path, 'w') as cjw:
        cjw.write(code.replace("{{table_body}}", "".join(["""
            <tr onclick="selectpoc({num},16)">
            <td scope="row">{num}</td>
            <td>{pwd}</td>
            <td>{t}</td>
            </tr>
            """.format(num=res[0], pwd=res[1], t=res[-1]) for res in result]))
                  .replace("{{poc_images}}", "".join(["""
            <img class="img-fluid poc{n}" src="{poc_path}" style="display:none">
            """.format(app_name=base_config.get("application_name"), n=res[0] ,poc_path=res[2].split("/")[-1]) for res in result])))


    browser.get("file:///" + os.getcwd() + "/"+ path)

    time.sleep(2)

    browser.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-last-child(2) td:nth-child(1)").click()
    time.sleep(2)
    base_reusables.take_screenshot("Weak Lockout/POC/", "loginfail.png", config)
    browser.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-last-child(1) td:nth-child(1)").click()
    time.sleep(2)
    base_reusables.take_screenshot("Weak Lockout/POC/", "loginpass.png", config)
    browser.quit()
