import urllib.request
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'https://www.baidu.com'

# 快代理（国内普通代理）：https://www.kuaidaili.com/free/intr/
proxies_poo = [
    {'http': '121.232.148.224:3256'},
    {'http': '183.247.152.98:53281'}
]

request = urllib.request.Request(url=url, headers=headers)

proxies = random.choice(proxies_poo)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')
with open('file/proxy_pool.html', 'w', encoding='utf-8') as f:
    f.write(content)