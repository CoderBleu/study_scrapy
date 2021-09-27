'''
下载驱动链接：http://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.63/
'''

from selenium import webdriver

# 创建浏览器操作对象
path = 'file/chromedriver.exe'

browser = webdriver.Chrome(path)

# 访问网站
# url = 'https://www.baidu.com'
#
# browser.get(url)

url = 'https://www.jd.com/'

browser.get(url)

# page_source获取网页源码
content = browser.page_source
print(content)

