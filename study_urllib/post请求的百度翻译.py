import urllib.request
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}
# post请求的参数 必须要进行编码.
# 注意： POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数，必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

# 把json对象变成json数据
obj = json.loads(content)
print(obj)