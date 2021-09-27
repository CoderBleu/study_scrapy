'''
星巴克：https://www.starbucks.com.cn/menu/
'''

from bs4 import BeautifulSoup

import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

# <ul class="grid padded-3 product"> 下的 strong
name_list = soup.select('ul[class="grid padded-3 product"] strong')

print(name_list)

for name in name_list:
    # print(name.get_text())
    print(name.string)

