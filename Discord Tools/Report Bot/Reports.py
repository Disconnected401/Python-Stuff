import requests
from colorama import Fore
import json
import time

R = Fore.RED
Y = Fore.YELLOW
green = Fore.GREEN
W = Fore.WHITE
gray = Fore.LIGHTBLACK_EX

report_delay = 1

def user_report(token, target):
    global report_delay
    url = "https://discordapp.com/api/v9/reporting/user"
    headers_template = {
        "accept": "*/*",
        "accept-language": "pl",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"24\", \"Chromium\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "Europe/Warsaw",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTczIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoicGwiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTczIENocm9tZS8xMjguMC42NjEzLjE4NiBFbGVjdHJvbi8zMi4yLjIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMyLjIuMiIsIm9zX3Nka192ZXJzaW9uIjoiMjI2MzEiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNTEyNDcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjU1OTkzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }

    data = {
        "version": "1.0",
        "variant": "1",
        "language": "en",
        "breadcrumbs": [48, 10, 8, 12],
        "elements": {"user_profile_select": ["photos",  "name",  "descriptors"]},
        "user_id": target,
        "name": "user"
    }

    headers = headers_template.copy()
    headers["authorization"] = token
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    token_parts = token.split('.')
    masked_token = token_parts[0] + '#' + '#' * len(token_parts[1]) + '#' + '#' * len(token_parts[2])
    
    if response.status_code == 429:
        print(f"[{R}-{W}] Token > {gray}{masked_token}{W} Status Code > {gray}{response.status_code}{W}")
        print(f"[{Y}!{W}] Rate limited, waiting 30 seconds")
        report_delay += 0.5
        print(f"[{Y}!{W}] Delay increased to", report_delay)
        time.sleep(30)
    else:
        print(f"[{green}+{W}] Token > {gray}{masked_token}{W} Status Code > {gray}{response.status_code}{W}")
    time.sleep(report_delay)