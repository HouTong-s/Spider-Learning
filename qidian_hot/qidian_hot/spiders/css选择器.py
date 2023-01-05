#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider
class CSS_Spider(Spider):
    #定义爬虫名称
    name = 'css'
    #起始的URL列表
    #start_urls = ["https://www.qidian.com/rank/hotsales/page1/"]
    #获取初始Request
    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales/page1/"
        #生成请求对象，设置url, headers, callback
        yield Request(url,callback=self.qidian_parse)
    # 使用CSS选择器解析数据
    def qidian_parse(self, response):
        #使用CSS定位到小说内容的div元素，生成选择器，并保存到选择器列表中
        list_selector = response.css("[class='book-mid-info']")
        #依次读取每部小说，从中获取小说名称、作者、类型和形式
        for one_selector in list_selector:
            #获取小说名称
            name = one_selector.css("h2>a::text").extract_first()
            #获取作者
            author = one_selector.css(".author a::text").extract()[0]
            #获取类型
            type = one_selector.css(".author a::text").extract()[1]
            #获取形式（连载还是完本）
            form = one_selector.css(".author span::text").extract_first()
            #将爬取到的一部小说保存到字典中
            hot_dict = {"name":name,                  #小说名称
                        "author":author,               #作者
                        "type":type,                    #类型
                        "form":form}                    #形式
            #使用yield返回字典
            yield hot_dict