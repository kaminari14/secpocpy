import time
from Vulns import clickjacking, secure_httponly, concurrent_sessions, username_enumration, browser_cache, session_deletion, session_fixation
from reusables import os_reusables, base_reusables
import getopt, sys

print('''
___  ___  ___ _ __   ___   ___ _ __  _   _ 
/ __|/ _ \/ __| '_ \ / _ \ / __| '_ \| | | |
\__ \  __/ (__| |_) | (_) | (__| |_) | |_| |
|___/\___|\___| .__/ \___/ \___| .__/ \__, |
            | |              | |     __/ |
            |_|              |_|    |___/ 
By Kaminari14 - https://github.com/kaminari14
''')

print('This tool does not say with certainty if a vulnurability is present or not. Please look at the POCs and decide if manual intervention is needed.\n\n')



def get_help():
    print('USAGE: python -m secpoc.py [-i test1,test2,test3,...] [-x 1,2,3,...] [-h] [--config=</path/to/config>]')
    print('-h'.ljust(18)+": help")
    print('-i 1,2,3...'.ljust(18)+ ': Include  only the tests mentioned. options available')
    print(''.ljust(20)+'1. Session Deletion')
    print(''.ljust(20)+'2. Clickjacking')
    print(''.ljust(20)+'3. Concurrent Sessions')
    print(''.ljust(20)+'4. Secure / HTTPOnly Flag')
    print(''.ljust(20)+'5. Browser Cache')
    print(''.ljust(20)+'6. Username_enumration')
    print(''.ljust(20)+'7. Session Fixation')
    print('-x 1,2,3...'.ljust(18)+': Exclude the tests mentioned. options available')
    print(''.ljust(20)+'1. Session Deletion')
    print(''.ljust(20)+'2. Clickjacking')
    print(''.ljust(20)+'3. Concurrent Sessions')
    print(''.ljust(20)+'4. Secure / HTTPOnly Flag')
    print(''.ljust(20)+'5. Browser Cache')
    print(''.ljust(20)+'6. Username_enumration')
    print(''.ljust(20)+'7. Session Fixation')




def main(argv):


    vulns = [session_deletion.session_deletion,
            clickjacking.clickjacking,
            concurrent_sessions.concurrent_sessions,
            secure_httponly.httponly_secure,
            browser_cache.browser_cache,
            username_enumration.username_enumration,
            session_fixation.session_fixation,
            ]


    try:
        opts, args = getopt.getopt(argv,"hvi:x:",["config=",])
    except getopt.GetoptError:
        get_help()  
        quit()  
    
    to_execute=[]
    config_file = None

    for arg in args:
        argdata=arg.split('=')
        if argdata[0]=='config':
            config_file=argdata[1]

    for opt, arg in  opts:
        if opt == '-h':
            get_help()
        if opt == '--config':
            config_file = arg
        if opt == '-i':
            for i in arg.split(','):
                if i:
                    to_execute.append(vulns[int(i)-1])
            
        if opt == '-x':
            for j in range(len(vulns)):
                if j+1 not in [int(i) for i in arg.split(',')]:
                    to_execute.append(vulns[int(j)])
    
    if not config_file:
        print('Config file not mentioned. Use --config')
        get_help()
        quit()
    
    config_data = base_reusables.get_config_data(config_file)
    env_data = base_reusables.get_config_data('./config_files/env_config.ini')
    config = {'application_data': dict(config_data.items('base')), 
        'login' :dict(config_data.items('login')), 
        'screen_info': dict(env_data.items('screen_info')),
        'firefox': dict(env_data.items('firefox'))
    }


    if 'application_data' not in config.keys():
        print('Invalid or Missing Config File')
        get_help()
        quit()
    os_reusables.makedirectory('./POCs/' + config['application_data'].get('application_name'))

    if not to_execute:
        for vuln in vulns:
            vuln(config=config)
    else:
        for vuln in to_execute:
            vuln(config=config)



if __name__ == "__main__":
    main(sys.argv[1:])