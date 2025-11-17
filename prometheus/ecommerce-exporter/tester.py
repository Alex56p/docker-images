import json
from urllib.parse import urlparse

import httpx
import parsel

import sys

print("Args:", sys.argv)

url = sys.argv[1]
selector_text = sys.argv[2]

BASE_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US;en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
}


query_response = httpx.get(url=url, headers=BASE_HEADERS, follow_redirects=True).text
print(query_response)
selector = parsel.Selector(text=query_response)
selector_match = selector.css(selector_text).get()

print("match:", selector_match)

