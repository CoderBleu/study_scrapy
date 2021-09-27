import requests

'''
代理
快代理：https://www.kuaidaili.com/free/intr/
'''

url = 'http://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'wd': 'ip'
}

proxy = {
    'http': '113.100.209.100:3128'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

# 以字符串的形式返回了网页的源码
content = response.text

with open('file/daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
