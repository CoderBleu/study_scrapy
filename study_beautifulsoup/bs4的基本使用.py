from bs4 import BeautifulSoup

# 默认打开的文件的编码格式是gbk，所以需要指定编码
soup = BeautifulSoup(open('file/bs4_demo.html', encoding='utf-8'), 'lxml')

# 获取html内容
print(soup)
# 根据标签名找，找到第一个符合条件的标签返回，并获取标签的属性和属性值
print(soup.li.attrs)

# find
# 返回的是第一个符合条件的数据
# <li class="c">1</li>
print(soup.find('li'))

# 根据title的值来找到对应的标签对象
# <li class="b">3</li>
print(soup.find('li', class_='b'))

# find_all 返回的是一个列表，并且返回了所有的a标签
# [<li class="c">1</li>, <li class="a">2</li>, <li class="b">3</li>, <li class="li_c" id="c">c</li>, <li id="c1">c1</li>]
print(soup.find_all('li'))
# 多个就是列表数据，并限制返回条数：[<p id="p">我是p标签</p>, <li class="c">1</li>]
print(soup.find_all(['li', 'p'], limit=2))

# select推荐
# select方法返回的是一个列表，并且会返回多个数据
print(soup.select('li'))

# 可以通过.代表class,我们把这种操作叫做类选择器
print(soup.select('.a'))

# 可以通过#代表id,我们把这种操作叫做id选择器
print(soup.select('#p'))

# 属性选择器
# 查找到li标签中有id的标签
print(soup.select('li[id]'))

# 查找到li标签中有id为c1的标签
print(soup.select('li[id="c1"]'))

print("--------------层级选择器----------")

# 层级选择器
# 后代选择器
# 找到的是div下面的li
print(soup.select('ul li'))

print("--------------子代选择器----------")
# 子代选择器
# 某标签的第一级子标签,不会查ul下div中的li标签
print(soup.select('ul > li'))

# 找到li标签和p标签所有的对象
print(soup.select('li,p'))

print("--------------节点信息----------")
# 获取节点内容
obj = soup.select('#p')[0]

# 如果标签对象中，只有内容，那么string和get_text()都可以使用
# 如果标签对象中，除了内容还有标签，那么string就获取不到数据，而get_text()是可以获取数据
print(obj.string)
print(obj.get_text()) # 推荐

# 节点的属性
print('------------节点的属性-----------')
obj = soup.select('p')
print(obj)
obj = soup.select('p')[1]
print(obj.attrs.get('class'))
