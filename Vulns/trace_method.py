from reusables import base_reusables, os_reusables, webdriver_reusables
import requests, os, time
from html import escape

def trace_method(config):

    print('[+] Starting test for Trace Method')

    application_data = config.get('application_data')
    browser = webdriver_reusables.initialise_webdriver(config)
    os_reusables.makedirectory('./POCs/'+ application_data.get('application_name') + '/Trace_Method/')
    for method in ['TRACE','TRACK']:

        request = requests.Request('TRACE' if method=='TRACE' else 'TRACK', application_data.get('url'))
        req= request.prepare()
        ses = requests.Session()
        response = ses.send(req)
        req_data = method + " " + application_data.get('url')
        res_data = str(response.status_code) + ' ' + str(response.reason) + '</br></br>'



        for header, value in response.headers.items():
            res_data += header + " : " + value  + "</br>"

        res_data += '</br></br>' + escape(response.text)

        path = 'POCs/' + application_data.get('application_name') + '/Trace_Method/options_tampering_' + method + '.html'

        with open('./HTML/rr_template.html', 'r') as vbt:
            code = vbt.read()
        with open(path, 'w') as vbt:
            vbt.write(code.replace(r'{{request}}', req_data).replace(r'{{response}}', res_data))



        browser.get("file:///" + os.getcwd() + "/"+ path)

        time.sleep(2)

        base_reusables.take_screenshot("Trace_Method/", method+ ".png", config)

    browser.quit()

    print('Finished')