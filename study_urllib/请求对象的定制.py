import urllib.request

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'http://www.baidu.com'
# 封装一个Request对象
request = urllib.request.Request(url=url, headers=headers)
# Open the URL url, which can be either a string or a Request object.
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)