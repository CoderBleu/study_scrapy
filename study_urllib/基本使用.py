import urllib.request

# 定义一个url
# url = 'http://www.baidu.com'
url = 'http://www.coderblue.cn'

# 模拟浏览器向服务器发送请求并响应
response = urllib.request.urlopen(url)

# 获取响应中的页面的源码内容，read方法返回的是字节形式的二进制数据
content = response.read()

# 将二进制转换成utf编码格式
content = content.decode('utf-8')

print(content)
