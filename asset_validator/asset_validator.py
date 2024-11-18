#!/usr/bin/env python3


from requests import get
from urllib3 import disable_warnings
from sys import stdin, argv
from colorama import Fore
from urllib.parse import unquote
from requests.exceptions import ConnectionError
def validate():
    disable_warnings()
    for assets in stdin:
        asset = assets.rstrip()
        if len(asset) != 0:
            try:
                r = get(asset, verify=False, allow_redirects=True)
                handle_response(r, asset)
            except ConnectionError as e:
                print(e)

def handle_response(r, asset): 
    if str(r.status_code) == str(200):
        print(f"GIVEN URL - [{asset}]")
        print(f"REQUESTED - [{unquote(r.url)}]")
        print(Fore.WHITE + f"STAT CODE - [{r.status_code}] " + Fore.RESET + f"Size - [{len(r.text)}]")
        print("")
    else:
        if len(argv) > 1:
            if str(argv[1]) == str(r.status_code):
                pass
            else:
                print(f"GIVEN URL - [{asset}]")
                print(f"REQUESTED - [{unquote(r.url)}]")
                print(Fore.RED + f"STAT CODE - [{r.status_code}] " + Fore.RESET + f"Size - [{len(r.text)}]")
                print("")
        else:
            print(f"GIVEN URL - [{asset}]")
            print(f"REQUESTED - [{unquote(r.url)}]")
            print(Fore.RED + f"STAT CODE - [{r.status_code}] " + Fore.RESET + f"Size - [{len(r.text)}]")
            print("")

validate()

