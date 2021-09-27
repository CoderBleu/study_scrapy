# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ReadbookPipeline:
    def open_spider(self, spider):
        self.fp = open('../file/movie.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 获取item对象中result的JSON值
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行完之后，执行的方法
    def close_spider(self, spider):
        self.fp.close()


# 加载settings文件
from scrapy.utils.project import get_project_settings
# pip3 install pymysql
import pymysql


class MysqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.username = settings['DB_USERNAME']
        self.password = settings['DB_PASSWORD']
        self.db_name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.connection = pymysql.connect(host=self.host, user=self.username, password=self.password,
                                          database=self.db_name, charset=self.charset, autocommit=False)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql = '''
                INSERT INTO book(name, src) values ("{}","{}")
            '''.format(item['name'], item['src'])
        self.cursor.execute(insert_sql)  # 插入
        self.connection.commit()

    def close_spider(self, spider):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.connection.close()
