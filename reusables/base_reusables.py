import mss
from screeninfo import get_monitors
from reusables import os_reusables
from configparser import RawConfigParser
import time

def take_screenshot(directory_path, filename, config_file, sleep = 0):
    time.sleep(sleep)
    base_conf = get_config_data('base',config_file)
    monitor_res = get_monitors()[0]
    directory = './POCs/' + base_conf.get('application_name') + "/" + directory_path
    os_reusables.makedirectory(directory)
    with mss.mss() as sct:
        mon = sct.monitors[2]
        monitor = {
            "top": mon["top"] + 40,  
            "left": mon["left"], 
            "height": monitor_res.height - 40,
            "width": monitor_res.width,
            "mon": 2,
        }

        sct_img = sct.grab(monitor)


        mss.tools.to_png(sct_img.rgb, sct_img.size, output=directory+filename)


def get_config_data(config_key,  config_file):
    try:
        config = RawConfigParser()
        config.read(config_file)
    except:
        return None
    return dict(config.items(config_key))