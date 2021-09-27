import requests

'''
1、参数可以使用params传递
2、参数无需urlencode编码
3、不需要请求对象的定制
4、请求资源路径中的？可加可不加
'''

url = 'http://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'wd': '北京'
}

response = requests.get(url=url,params=data,headers=headers)

# 以字符串的形式返回了网页的源码
print(response.text)
