from lxml import etree

# 解析本地文件
tree = etree.parse('demo.html')

# etree.HTML(response.read().decode('utf-8'))

li = tree.xpath('//li[@id]')

# 查找所有有id的属性的li标签
# text()获取标签中的内容
li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为c的li标签，注意引号问题
li_list_id = tree.xpath('//ul/li[@id="c"]/text()')

# 找到id为c的li标签的class的属性值
li_list_class = tree.xpath('//ul/li[@id="c"]/@class')

# 找到id为c且id包含c的li标签
li_list_contains = tree.xpath('//ul/li[contains(@id, "c")]/text()')

# 找到id为c且id以c开头的li标签
li_list_starts_with = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')

# 查询id的值为c和class为li_c
li_list_id_class = tree.xpath('//ul/li[@id="c" and @class="li_c"]/text()')

# 查询id为c或者class为a的li标签
list_list_id_or_class = tree.xpath('//ul/li[@id="c"]/text() | //ul/li[@class="a"]/text()')


print(list_list_id_or_class)
print(len(li_list_class))
