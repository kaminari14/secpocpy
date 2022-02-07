# secpocpy
Automation tool for basic Web PT POCs

## Installation
```
pip install -r requirements.txt
```

## Basic Configuration

1. Create a new firefox profile for automation.
2. Open firefox with the new automation profile and detatch the developer tools. This step is needed for getting proper screenshots for POCs.
3. In the config_files folder the following `env_config.ini` file should be placed.
```
[screen_info]
monitor = 0

[firefox]
webdriver_location = path/to/webdriver/file
profile_location = path/to/new//firefox/profile
firefox_location = path/to/firefox/executable
```

## Application Configuration

The application configuration file should look something like this

```
[base]
url = <rl of the application>
application_name = <name of the aplication>


[login]
username = <first username for login>
password = <password for the first username>
username_css = <css selector for username field>
password_css = <css selector for password field>
logout_css = <css selector for logout button>
submit_css = <css selector for submit button>
url = <url that contains the login field>
access_controlled_url = <any url that needs authentication>
username2 = <second username for login>
pass2 = <password for the second username>
```
  
## Basic Usage

```
python -m secpoc.py [-i 1,2,3,...] [-x 1,2,3,...] [-h] [--config=</path/to/application/config/file>]
```
