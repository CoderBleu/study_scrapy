import scrapy

from crawl_movie.items import CrawlMovieItem


class MovieHeavenSpider(scrapy.Spider):
    name = 'movie_heaven'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 第一个的名字和第二页的图片 //div[@class="co_content8"]/tr[2]///td[2]//a[1]
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[1]')

        for a in a_list:
            # 获取第一页的name 和 超链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.dytt8.net' + href

            # 第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})


    def parse_second(self, response):
        # 注意：如果拿不到数据的情况下，一定检查你的xpath语法是否正确
        # 标签是相连的父子层级可使用/：//div[@id="Zoom"]/span/img/@src
        # 标签是有隔断的层级使用 //
        src = response.xpath('//div[@id="Zoom"]//img//@src').extract_first()
        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        movie = CrawlMovieItem(src=src, name=name)

        yield movie