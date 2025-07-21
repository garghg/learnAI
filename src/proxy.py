# Reference - Yicong: https://github.com/ohyicong/Tor/blob/master/create_basic_tor_proxy.py

import os
import stem.process
import re
import requests
import json
from datetime import datetime


SOCKS_PORT = 9050
TOR_PATH = os.path.normpath(os.getcwd()+"./tor.exe")

def startProxy(PROXIES):
    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': str(SOCKS_PORT),
        },
        init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
        tor_cmd = TOR_PATH
    )
    response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    result = json.loads(response.content)
    print('TOR IP [%s]: %s %s'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))

    return tor_process

def stopProxy(process):
    process.kill()