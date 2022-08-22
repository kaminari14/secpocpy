from reusables import base_reusables, os_reusables, webdriver_reusables
import requests, os, time


def verb_tampering(config):

    print('[+] Starting test for  Verb tampering')

    application_data = config.get('application_data')
    browser = webdriver_reusables.initialise_webdriver(config)
    os_reusables.makedirectory('./POCs/'+ application_data.get('application_name') + '/Verb_Tampering/')
    for method in ['HEAD','OPTIONS']:

        response = requests.head(application_data.get('url')) if method == 'HEAD' else requests.options(application_data.get('url'))
        req_data = method + " " + application_data.get('url')
        res_data = str(response.status_code) + ' ' + str(response.reason) + '</br></br>'

        for header, value in response.headers.items():
            res_data += header + " : " + value  + "</br>"


        path = 'POCs/' + application_data.get('application_name') + '/Verb_Tampering/options_tampering_' + method + '.html'

        with open('./HTML/rr_template.html', 'r') as vbt:
            code = vbt.read()
        with open(path, 'w') as vbt:
            vbt.write(code.replace(r'{{request}}', req_data).replace(r'{{response}}', res_data))



        browser.get("file:///" + os.getcwd() + "/"+ path)

        time.sleep(2)

        base_reusables.take_screenshot("Verb_Tampering/", method+ "_VerbTampering.png", config)

    browser.quit()

    print('Finished')