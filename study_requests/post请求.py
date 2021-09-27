import requests
import json

'''
1、post请求 是不需要编解码
2、post请求的参数是data
3、不需要请求对象的定制
'''


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'eye'
}

response = requests.post(url=url,data=data,headers=headers)

# 获取响应的数据
content = response.text

# 把json对象变成json数据
obj = json.loads(content,encoding='utf-8')
print(obj)
