import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dang_dang_net']
    start_urls = ['http://dang_dang_net/']

    def parse(self, response):
        pass
