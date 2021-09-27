import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from readbook.items import ReadbookItem


class ReadBookNetSpider(CrawlSpider):
    name = 'read_book_net'
    allowed_domains = ['www.dushu.com']
    # 注意第一页起始位置
    start_urls = ['https://www.dushu.com/book/1617_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'book/1617_\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath("//div[@class='bookslist']//img")

        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            book = ReadbookItem(name=name, src=src)
            yield book
