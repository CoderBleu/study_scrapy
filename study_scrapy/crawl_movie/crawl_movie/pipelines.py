# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlMoviePipeline:
    def open_spider(self, spider):
        self.fp = open('file/movie.json', 'a', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 获取item对象中result的JSON值
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行完之后，执行的方法
    def close_spider(self, spider):
        self.fp.close()
