import scrapy
import json


class TranslatePostSpider(scrapy.Spider):
    name = 'translate_post'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    start_urls = ['https://fanyi.baidu.com/sug']

    # def parse(self, response):
    # post请求跟这个get请求的parse没任何关系
    # Post请求
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'love'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        # obj = json.loads(content, encoding='utf-8')
        obj = json.loads(content)

        print(obj)
