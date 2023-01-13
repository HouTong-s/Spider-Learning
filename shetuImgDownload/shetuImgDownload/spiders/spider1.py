#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider                      #导入Spider类
from shetuImgDownload.items import ShetuimgdownloadItem  #导入Item
class ImageDownloadSpider(Spider):
    #定义爬虫名称
    name = 'img'
    #获取初始Request
    def start_requests(self):
        url = "https://699pic.com/photo/"
        #生成请求对象
        yield Request(url)

    #解析函数-解析照片列表页，获取各个主题对应详情页的URL
    def parse(self, response):
        #使用XPath定位到每个主题对应的URL
        urls = response.xpath("//div[@class='pl-list']/a[1]/@href").extract()
        #遍历每个URL
        for i in range(len(urls)):
            #使用URL构造Request请求并返回
            yield Request("https:"+urls[i], callback=self.parse_image)

    #解析函数-解析详情页，获取照片URL
    def parse_image(self, response):
        #创建ShetuImageDownloadItem对象
        item = ShetuimgdownloadItem()
        #获取所有照片的URL地址
        urls = response.xpath("//li[@class='list']/a/img/@data-original").extract()
        length = len(urls)
        if  length> 0:#如果获取到照片URL
            #照片主题名称
            for i in range(length):
                urls[i] = "https:"+urls[i]
            title = response.xpath("//li[@class='list']/a/img/@title").extract_first()
            item["title"] = title                    #保存照片主题名称
            #将图片的URL地址保存到key为images_urls的Item中
            item["image_urls"] = urls
            yield item
            #获取下一页URL
            next_url = response.xpath("//a[@class='downPage']/@href").extract()
            if next_url:                               #如果获取到下一页的URL
                next_url = response.urljoin(next_url[0])       #绝对路径
                #使用下一页URL构造Request请求
                yield Request(next_url, callback=self.parse_image)