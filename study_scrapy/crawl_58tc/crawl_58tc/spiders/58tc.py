import scrapy
import ipython


class A58tcSpider(scrapy.Spider):
    name = '58tc'
    allowed_domains = ['https://sz.58.com/job/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=job_B,uuid_4beb867191154da6bddac3d4a475b5dc,displocalid_4,from_9224,to_jump,tradeline_job,jianzhi_B&final=1']
    start_urls = ['https://sz.58.com/job/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=job_B,uuid_4beb867191154da6bddac3d4a475b5dc,displocalid_4,from_9224,to_jump,tradeline_job,jianzhi_B&final=1/']

    def parse(self, response):
        # 获取的是字符串
        print(response.text)
        # 获取的是二进制
        # print(response.text)

        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        # 提取selector对象的data属性值
        print(span.extract())
        pass
