import scrapy



class BaiduSpider(scrapy.Spider):
    # 允许访问的域名
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址 指的是第一次要访问的域名
    # start_urls 是 http://后面再加/
    start_urls = ['http://www.baidu.com/']

    # 是执行了start_urls之后 执行的方法，方法中的response就是返回的那个对象
    # 相当于 response = urllib.request.urlopen(), response  = requests.gett()
    def parse(self, response):
        print('我的第一个scrapy项目')
