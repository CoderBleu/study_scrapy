import scrapy
from dangdang.items import DangdangItem


class DangDangNetSpider(scrapy.Spider):
    name = 'dang_dang_net'
    # 如果是多页下载的话，那么必须要调整的是allowed_domains的范围
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.36.04.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    # 定义初始页面
    page = 1


    # 原
    # def parse(self, response):
    #     # 懒加载：图片 //ul[@id='component_59']//li//img//@data-original
    #     # //ul[@id='component_59']//li//img//@src
    #     # //ul[@id='component_59']//li//img//@alt
    #     # 获取p标签下第一个span的值
    #     # //ul[@id='component_59']//li//p[@class="price"]/span[1]/text()
    #
    #     li_list = response.xpath('//ul[@id="component_59"]/li')
    #
    #     for li in li_list:
    #         img_src = li.xpath('.//img/@data-original').extract_first()
    #         # 第一张图片(None)和其他的图片的标签的属性呢是不一样的
    #         # 第一张图片的src是可以使用的，其他的图片的地址是data-original
    #         if img_src:
    #             img_src = img_src
    #         else:
    #             img_src = li.xpath('.//img/@src').extract_first()
    #             print('我是第一张图片：' + str(img_src))
    #
    #         name = li.xpath('.//img/@alt').extract_first()
    #         price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
    #         print(img_src, name, price)
    #
    #         book = DangdangItem(img_src=img_src, name=name, price=price)
    #
    #         # 获取一个book对象就将book交给pipelines,即return一个返回值
    #         yield book
    #         pass

    # 优化
    def parse(self, response):
        # 懒加载：图片 //ul[@id='component_59']//li//img//@data-original
        # //ul[@id='component_59']//li//img//@src
        # //ul[@id='component_59']//li//img//@alt
        # 获取p标签下第一个span的值
        # //ul[@id='component_59']//li//p[@class="price"]/span[1]/text()

        li_list = response.xpath('//ul[@id="component_59"]/li')

        result = []
        for li in li_list:
            img_src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片(None)和其他的图片的标签的属性呢是不一样的
            # 第一张图片的src是可以使用的，其他的图片的地址是data-original
            if img_src:
                img_src = img_src
            else:
                img_src = li.xpath('.//img/@src').extract_first()
                # print('我是第一张图片：' + str(img_src))

            name = li.xpath('.//img/@alt').extract_first()
            # 处理图片名非法字符
            if (str(name).find('/') != -1):
                name = str(name).replace('/', '-')
            if (str(name).find(':') != -1):
                name = str(name).replace(':', '-')
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            item = {'img_src': img_src, 'name': name, 'price': price}
            result.append(item)

            pass

        # print(result)
        book = DangdangItem(result=result)
        yield book

        # 拉取百页数据
        if self.page < 100:
            self.page = self.page + 1

            url = self.base_url + str(self.page) + '-cp01.36.04.00.00.00.html'

            # 调用parse方法，scrapy.Request就是scrapy的get请求，url就是请求地址，
            # callback是你要执行的那个函数，注意不要加()
            yield scrapy.Request(url=url, callback=self.parse)
