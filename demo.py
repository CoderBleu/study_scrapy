#导入urllib.request模块
import urllib.request
import requests

#设置请求头
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
#创建一个opener
opener=urllib.request.build_opener()
#将headers添加到opener中
opener.addheaders=[headers]
#将opener安装为全局
urllib.request.install_opener(opener)
#用urlopen打开网页
data=urllib.request.urlopen('https://acgaa.cyou/ptl.php?mb=ptl&pages=MTYzMDU5NzU5MA').read().decode('utf-8','ignore')
print(data)

# proxies = {
#     'http':'201.69.7.108:9000',
# }
# response = requests.get('http://sssss.cyou/C2B7767F',proxies=proxies)
# print(response.content)