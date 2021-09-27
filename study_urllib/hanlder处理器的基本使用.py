import urllib.request
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'https://www.baidu.com'

request = urllib.request.Request(url=url, headers=headers)

# post的请求的参数，必须要进行编码
handler = urllib.request.HTTPHandler()

# 模拟浏览器向服务器发送请求
opener = urllib.request.build_opener(handler)

# 获取响应的数据
response = opener.open(request)
content = response.read().decode('utf-8')

print(content)