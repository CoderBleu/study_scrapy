# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

'''
定义需要下载的数据
'''

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # # 原===================
    # 图片
    # img_src = scrapy.Field()
    # # 名字
    # name = scrapy.Field()
    # # 价格
    # price = scrapy.Field()

    # 优化
    result = scrapy.Field()

    pass


