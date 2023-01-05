#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider             #导入Spider类
from qidian_hot.items import QidianHotItem
class item_Spider(Spider):
    #定义爬虫名称
    name = 'item'
    #获取初始Request
    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales/page1/"
        #生成请求对象，设置url、headers和callback
        yield Request(url, callback=self.qidian_parse)
    #解析函数
    def qidian_parse(self, response):
        #使用xpath定位到小说内容的div元素，并保存到列表中
        list_selector = response.xpath("//div[@class='book-mid-info']")
        #依次读取每部小说的元素，从中获取小说名称、作者、类型和形式
        for one_selector in list_selector:
            #获取小说名称
            name = one_selector.xpath("h2/a/text()").extract_first()
            #获取作者
            author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
            #获取类型
            type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
            #获取形式（连载还是完本）
            form = one_selector.xpath("p[1]/span/text()").extract()[0]
            item = QidianHotItem()

            item["name"] = name
            item["author"] = author
            item["type"] = type
            item["form"] = form

            yield item