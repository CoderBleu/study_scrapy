import requests
from bs4 import BeautifulSoup

'''
古诗文网站：https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx
'''

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


# 获取页面源码
response = requests.get(url=url, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')
view_state = soup.select('#__VIEWSTATE')[0].attrs.get('value')
view_state_generator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

print(view_state)
print(view_state_generator)

img_code = soup.select('#imgCode')[0].attrs.get('src')
img_code_url = 'https://so.gushiwen.cn{}'.format(img_code)
print(img_code_url)

# 有坑，因为urllib.request跟requests不属于同一次请求，所以得到的验证码不一致
# import urllib.request
# urllib.request.urlretrieve(url=img_code_url,filename='file/验证码.jpg')

session = requests.session()
# 验证码的url的内容
response_code = session.get(img_code_url)
# 注意此时要使用二进制数据，因为我们要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件
with open('file/验证码.jpg', 'wb') as fp:
    fp.write(content_code)

verification_code = input('请输入验证码：')

login_url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

request_data = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1453669976@qq.com',
    'pwd': '123456',
    'code': verification_code,
    'denglu': '登录'
}

# 保证请求是同一个
# response_content = requests.post(url=login_url_post, headers=headers, data=request_data)
response_content = session.post(url=login_url_post, headers=headers, data=request_data)

with open('file/gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(response_content.text)
