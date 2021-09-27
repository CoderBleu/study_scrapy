# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


# 如果想使用管道的话，那么就必须在setting中开启管道 ITEM_PIPELINES
class DangdangPipeline:

    # 原:
    # item就是yield后面的book对象
    # def process_item(self, item, spider):
    #     # 以下这种模式不推荐，因为每传递过来一个对象，那么就打开一次文件
    #     # 1、write方法必须要写一个字符串，而不能是其他的对象
    #     # 2、w模式，会每一个对象都打开一次文件，覆盖之前的内容
    #     # 3、a模式，会一次性写入所有
    #     with open('spiders/file/book.json', 'a', encoding='utf-8') as fp:
    #         fp.write(str(item))
    #     # self.fp.write(str(item))
    #     return item

    # 在爬虫文件开始的之前就执行的一个方法
    def open_spider(self, spider):
        # 位于dangdang下spiders下的file
        self.fp = open('spiders/file/book.json', 'a', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 获取item对象中result的JSON值
        self.fp.write(str(item['result']))
        return item

    # 在爬虫文件执行完之后，执行的方法
    def close_spider(self, spider):
        self.fp.close()


# 开启多条管道-下载图片
# 定义管道类，并在settings中开启管道
# ITEM_PIPELINES = {
#    # 管道可以有很多个，那么管道是由优先级的，优先级的范围是1到1000，值越小优先级越高
#    'dangdang.pipelines.DangdangPipeline': 300,
#    'dangdang.pipelines.DangdangDownloadpipeline': 301,
# }
class DangdangDownloadpipeline:
    pass
    def process_item(self, download_data, spider):
        for item in download_data['result']:
            print(item)
            img_url = 'http:' + item.get('img_src')
            img_name = './spiders/file/images/' + item.get('name') + '.jpg'
            urllib.request.urlretrieve(img_url, img_name)
