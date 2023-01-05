#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from qidian_hot.items import QidianHotItem
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'loader'
    #获取初始Request
    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales/page1/"
        #生成请求对象，设置url,  callback
        #callback默认为本类的parse()函数
        yield Request(url,callback=self.qidian_parse)
    #解析函数
    def qidian_parse(self, response):
        #使用xpath定位到小说内容的div元素，保存到列表中
        list_selector = response.xpath("//div[@class='book-mid-info']")
        #依次读取每部小说的元素，从中获取名称、作者、类型和形式
        for one_selector in list_selector:
            novel = ItemLoader(item=QidianHotItem(), selector=one_selector)
            #使用XPath选择器获取小说名称
            novel.add_xpath("name", "h2/a/text()")
            #使用XPath选择器获取作者
            novel.add_xpath("author", "p[1]/a[1]/text()")
            #使用XPath选择器获取类型
            novel.add_xpath("type", "p[1]/a[2]/text()")
            #使用CSS选择器获取小说形式（连载还是完本）
            novel.add_css("form", ".author span::text")
            #将提取好的数据load出来，并使用yield返回
            yield novel.load_item()