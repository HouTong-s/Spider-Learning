from scrapy import Request
from scrapy.spiders import Spider
class TicketsSpider(Spider):
    #定义爬虫名称
    name = 'tickets'
    #获取初始Request
    def start_requests(self):
        url = "https://kyfw.12306.cn/otn/resources/login.html"
        #生成请求对象，设置URL
        yield Request(url)
    def parse(self, response):
        return None