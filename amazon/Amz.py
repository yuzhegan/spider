# encoding='utf-8

# @Time: 2023-01-28
# @File: %
#!/usr/bin/env
import requests
from icecream import ic
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
# change cwd to current file dir

session = requests.Session()

# ==================== 1.0  US code session====================
headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,*/*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'anti-csrftoken-a2z': 'gDseJ7z1FruolG1l4bRc7Z6eaMQThpfuuX3LmqwAAAAMAAAAAGPVKNVyYXcAAAAA;hO1bhlKylde6GiGaBm2Asx6WCdde+IjCu8HRgBY1LQNTAAAAAGPVKNUAAAAB',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'session-id=141-8324378-3408564; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=133-9964420-2947024; session-token="4uvVDwnTor/E4Itenk4LSD2wBNatL5zSkdwVX6lVtnc2R8PbWwWpjWR53v7PtIQmPtrWCg4tHeZ2g8WIPU4MQ8Zz7fYDpRRkuch33Aj/zRteDQJx++Q7+36ZGp8CANYsDWCtD9ofUxlSuw9xYuGGFgwDja8UsmztEAWAUQPy7jyIcSvn2pM/jJ3cl+xLPXv2NrHq8oTah3Kv4D/FDzAcrQ/7HJrRgD8ci7I5T5QkXo4="; csm-hit=tb:JD25YD8VDSHNBJQP7MS5+s-JD25YD8VDSHNBJQP7MS5|1674914117160&t:1674914117160&adb:adblk_no',
    'device-memory': '4',
    'downlink': '1.3',
    'dpr': '0.8',
    'ect': '3g',
    'origin': 'https://www.amazon.com',
    'pragma': 'no-cache',
    'referer': 'https://www.amazon.com/',
    'rtt': '350',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '0.8',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"5.15.82"',
    'sec-ch-viewport-width': '893',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'viewport-width': '893',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('actionSource', 'glow'),
)

data = '{"locationType":"LOCATION_INPUT","zipCode":"52325","storeContext":"generic","deviceType":"web","pageType":"Gateway","actionSource":"glow"}'

# add headers to session
session.headers.update(headers)

response = session.post('https://www.amazon.com/portal-migration/hz/glow/address-change',
                        params=params, data=data)
# print(response.text)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.post('https://www.amazon.com/portal-migration/hz/glow/address-change?actionSource=glow', headers=headers, data=data)
# ==================== 2.0  get items list====================


params = (
    ('k', 'macbook case'),
    ('crid', '1YWGI5BSFG866'),
    ('sprefix', 'macbook case,aps,553'),
    ('ref', 'nb_sb_noss_1'),
)

response = session.get('https://www.amazon.com/s', params=params)
# with open('macbook_case.html', 'w') as f:
#     f.write(response.text)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.amazon.com/s?k=macbook+case&crid=1YWGI5BSFG866&sprefix=macbook+case%2Caps%2C553&ref=nb_sb_noss_1', headers=headers)
