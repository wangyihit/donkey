#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def download(url:str, cookies:dict):

    # cookies = {
    #     'ihkYnttrQXfVO': '56oM5OsA0dCnVmt_XNjaBssfsRMtF41WGH3equSPmXqMcnUXHxL.jHYJGhW4tJ9MAqqjkBRNEUWjIK8Bq87ttWA',
    #     'ihkYnttrQXfVP': '5RCnyrKw7zOLqqqDVqWpnmqctDW0czguTyScNn2v84.O.bd8W0j_Z8wNlTawinNny_7ngbXtxP1dOLYVbY4n3A9f2OmyTsQQbJXNs0tHwXI6U2LAkUZQk59kHozw4Y._HL40bQFjpVNVQ5p5vntHeH4v4XiCjwBpCSoP5uUGd74GkNqvuG86EkaE71h5_4u.VimdKg4tIlvvBBW749Aib3qLcOCumN2t6POeHKn56dk_itGDNHE8yKsIA04o5cufXx9PUSRM0XfY4lfMbesxCY4viffLZU5In9oBAJDQhsizQe2A4cayyP0ahEuXJQLex33hMqpH6ghwHxFHwM1vRjL',
    # }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,en-US;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'ihkYnttrQXfVO=56oM5OsA0dCnVmt_XNjaBssfsRMtF41WGH3equSPmXqMcnUXHxL.jHYJGhW4tJ9MAqqjkBRNEUWjIK8Bq87ttWA; ihkYnttrQXfVP=5RCnyrKw7zOLqqqDVqWpnmqctDW0czguTyScNn2v84.O.bd8W0j_Z8wNlTawinNny_7ngbXtxP1dOLYVbY4n3A9f2OmyTsQQbJXNs0tHwXI6U2LAkUZQk59kHozw4Y._HL40bQFjpVNVQ5p5vntHeH4v4XiCjwBpCSoP5uUGd74GkNqvuG86EkaE71h5_4u.VimdKg4tIlvvBBW749Aib3qLcOCumN2t6POeHKn56dk_itGDNHE8yKsIA04o5cufXx9PUSRM0XfY4lfMbesxCY4viffLZU5In9oBAJDQhsizQe2A4cayyP0ahEuXJQLex33hMqpH6ghwHxFHwM1vRjL',
        'Pragma': 'no-cache',
        'Referer': 'https://sugh.szu.edu.cn/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get('https://sugh.szu.edu.cn/', cookies=cookies, headers=headers)
    return response


if __name__ == '__main__':
    pass
