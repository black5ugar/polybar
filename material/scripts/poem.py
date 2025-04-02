"""
Poems of the day
thanks for 今日诗词 API: https://www.jinrishici.com
"""
import requests
import json

url = "https://v2.jinrishici.com:443/one.json"
cookies = {"X-User-Token": "Vh1elUeFAfDsYOjYWxbhq+QFW4Lw4PK7"}
headers = {
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/85.0.4183.121 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;\
                q=0.9,image/avif,image/webp,image/apng,*/*;\
                q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.jinrishici.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
}

try:
    res = requests.get(url, headers=headers, cookies=cookies)
    res.encoding = 'utf-8'

    # trans to the jsonobj
    text = res.text
    jsonobj = json.loads(text)

    # get the dynasty, author, and poem
    dynasty = jsonobj['data']['origin']['dynasty']
    author = jsonobj['data']['origin']['author']
    poem = jsonobj['data']['content']

    print(poem + "——" + dynasty + "·" + author)
except requests.exceptions.ConnectionError:
    print("尚未联网哦~")
