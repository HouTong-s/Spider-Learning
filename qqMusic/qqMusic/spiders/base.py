import scrapy
from scrapy import Request

class BaseSpider(scrapy.Spider):
    name = 'base'

    def start_requests(self):
        url = "https://y.qq.com/n/ryqq/toplist/4"
        yield Request(url)
    def parse(self, response):
        #print("返回为："+str(response.xpath('/html').extract_first()))
        #with open("1.txt","a",encoding="utf-8") as f:
            #f.write(str(response.xpath('/html').extract_first()))
        list_selector = response.xpath("//ul[@class='songlist__list']/li") 
        
        #list_selector = response.xpath("//div[@class='songlist__item']")
        print("长度为："+str(len(list_selector))) 
        for one_selector in list_selector:         
            name = one_selector.xpath("div/div[3]/span/a[2]/text()").extract_first()
            singer = one_selector.xpath("div/div[4]/a/text()").extract_first()            
            song_dict={"name":name,
                        "singer":singer}
            yield song_dict
    