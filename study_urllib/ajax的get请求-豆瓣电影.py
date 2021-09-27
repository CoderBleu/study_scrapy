import urllib.request
import json

import scrapy

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

# post的请求的参数，必须要进行编码
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')

# 数据下载到本地，open方法默认情况下使用的是gbk的编码，需要转换成utf-8
with open('file/douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)